#!/usr/bin/python
import os, sys, time, json, hashlib, threading
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.internet import task

import subprocess

if os.sep == '\\':
	__sevenzip__ = 'bin\\7za.exe'
	print 'windows'
else:
	__sevenzip__ = '7z'
	print 'linux'

def compress(self,fname):
	global __sevenzip__
	subprocess.Popen([__sevenzip__,'a','-t7z',fname+'.7z',fname])

class File:
	def __init__(self,name,fname):
		self.name = name
		self.fname = fname
		self.size = os.path.getsize(self.fname)
		
		self.info = {'name':name,'fname':fname,'size':self.size}
		
		self.fpos = 0

class Connection(LineReceiver):
	def __init__(self, node):
		self.node = node
		self.state = 'GETHND'
		self.last_seen = time.time()
		self.file_pos = 0
		
		self.name = ''

	def connectionMade(self):
		self.sendLine('get::hnd::null')
		self.host = self.transport.getHost()
	
	def connectionLost(self, reason):
		self.node.connections.remove(self)
		self.node.remove_client((self.host.host,self.name))
	
		if self.state=='GETHND': return
		
		if self.name: self.node.log('[client-%s] Disconnected' % (self.name))
		else: self.node.log('[client-%s] Disconnected' % (self.host.host))

	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}
	
	def sendLine(self, line):
		self.transport.write(line+'\r\n\r\n')
	
	def lineReceived(self, line):
		line = self.parse_line(line)
		#print line

		if line['com']=='put':
			if line['opt']=='hnd':
				#Shake hands if we haven't already.
				if self.state=='GETHND':
					self.sendLine('put::hnd::%s' % self.node.info['security'])
					self.name = line['val']
					self.state='GETPASSWD'
				else:
					self.sendLine('put::hnd::Already shook hands!')
			
			elif line['opt']=='pwd':
				if self.state=='GETPASSWD':
					if self.node.info['security']=='password': self.handle_PASSWORD(line['val'])
					elif self.node.info['security']=='auth': self.handle_AUTH(line['val'].split(':')[0],line['val'].split(':')[1])
			
			elif line['opt']=='png':
				self.last_seen = time.time()
			
			elif line['opt']=='bro':
				_n = tuple(line['val'].split(':'))
				
				if not _n in self.node.info['broadcasting']:
					self.node.info['broadcasting'].append(_n)
					self.node.log('[broadcast] Now broadcasting %s:%s' % _n)
					self.sendLine('put::bro::okay')
		
		elif line['com']=='get':
			if line['opt']=='inf':
				
				#Start our looping calls now.
				#Starts pinging clients
				l = task.LoopingCall(self.ping)
				l.start(10) #TODO: Make this a variable
				
				#TODO COMMENT: This might actually be a bad idea
				#If we did put this in, we'd have to tell the client
				#that the ping wouldn't be arriving at the expected time
				#and to hang on a bit longer before bailing out.
				
				#Sends a broadcast packet every <x> seconds
				l = task.LoopingCall(self.broadcast)
				l.start(self.node.info['broadcast_every'])
				
			elif line['opt']=='fil':
				_f = self.node.get_file(line['val'])
				
				if not _f:
					self.sendLine('put::fib::error')
					return
				
				if not _f.fpos:
					self.node.log('[client-%s] Getting file: %s' % (self.name,_f.name))
				
				with open(_f.fname, "rb") as f:
					f.seek(_f.fpos)
					
					byte = f.read(8100)
					_f.fpos+=len(byte)
					
					if len(byte):
						#byte = byte.replace('\r\r\n','<crlf>')
						self.sendLine('put::fil::%s' % byte)
					#else:
					#	#self.sendLine('put::fie::end')
					#	#self.node.log('[client-%s] Got file: %s' % (self.name,_f.name))
					#	_f.fpos = 0
		else:
			print 'Garbage: '+str(line)

	def handle_PASSWORD(self, passwd):
		if not hashlib.sha224(passwd).hexdigest()==self.node.info['passwd']:
			self.sendLine('put::pwd::wrong')
			return
		
		self.sendLine('put::pwd::okay')
		self.node.add_client((self.host.host,self.name))
	
	def handle_AUTH(self,usr,pas):
		if self.node.auth_user(usr,pas):
			self.sendLine('put::pwd::okay')
			self.node.add_client((self.host.host,self.name))
		else:
			self.sendLine('put::pwd::wrong')
	
	def ping(self):
		self.sendLine('get::pin::null')
		
		if time.time()-self.last_seen > 30:
			self.transport.loseConnection()
	
	def broadcast(self):
		self.sendLine('put::inf::%s' % (json.dumps(self.node.info)))

class Node(Factory):
	def __init__(self,info,parent=None):
		self.info = info
		
		self.parent = parent
		
		self.clients = []
		self.connections = []
		
		self.files = []
		self.populate_file_list()

	def log(self,text):
		if self.parent: self.parent.log(text)
		else: print text
	
	def stop(self):
		pass
	
	def populate_file_list(self):
		for root, dirs, files in os.walk(self.info['share_dir']):
			for infile in files:
				_fname = os.path.join(root, infile)
				file, ext = os.path.splitext(_fname)
				
				if os.path.getsize(_fname):
					_f = File(infile,_fname)
					
					self.files.append(_f)
					self.info['files'].append(_f.info)
					self.log('[Files] Sharing %s' % _fname)
	
	def auth_user(self,usr,pas):
		for user in self.parent.auth_db['users']:
			if user['usr']==usr and user['pas']==pas: return True
		
		return False
	
	def get_file(self,name):
		for file in self.files:
			if file.name==name:
				return file
		
		return False
	
	def has_client(self,who):
		for client in self.clients:
			if client['name']==who: return True
		
		return False
	
	def add_client(self,who):
		if not self.has_client(who):
			self.clients.append({'name':who})
			self.log('[client-%s] Connected' % who[1])
	
	def remove_client(self,who):
		for client in self.clients:
			if client['name']==who:
				self.clients.remove(client)
	
	def buildProtocol(self, addr):
		_c = Connection(self)
		self.connections.append(_c)
		
		return _c

class start_server(threading.Thread):
	def __init__(self,name='default',broadcast=False,searchable=False,network=None,passwd='22c7d75bd36e271adc1ef873aee4f95db6bc54a9c2f9f4bcf0cd18a8',parent=None,use_threading=True):
		self.parent = parent
		self.use_threading = use_threading
		
		#if self.use_threading:
		threading.Thread.__init__(self)
		#self.parent = parent
		
		_temp_info = ''
		
		_f = open('node.conf','r')
		for line in _f.readlines():
			_temp_info += line.replace('\n','')
		_f.close()
		
		self.info = json.loads(_temp_info)
		self.info['files'] = []
		self.info['broadcast_every'] = int(self.info['broadcast_every'])
		self.info['security'] = str(self.info['security'])
		
		if self.info['security']=='auth':
			_adb = open(self.info['authdb'],'r')
			self.auth_db = json.loads(_adb.readline())
			_adb.close()
		
		if self.info['broadcast']:
			self.info['broadcasting'] = []
		
		self.node = None
		self.running = False
	
	def log(self,text):
		print text
	
	def start(self):
		if self.use_threading:
			threading.Thread.start(self)
		else:
			self.run()
	
	def run(self):
		_n = Node(self.info,parent=self)
		reactor.listenTCP(9001, _n)
		self.reactor = reactor
		self.node = _n
		
		self.running = True
		
		if self.use_threading:
			reactor.run(installSignalHandlers=0)
		else:
			reactor.run()
	
	def stop(self):
		self.node.stop()
		reactor.stop()
		reactor.disconnectAll()
		
		self.running = False

if __name__ == "__main__":
	start_server(use_threading=False).start()
