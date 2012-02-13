#!/usr/bin/python
import os, sys, time, copy, json, hashlib, threading
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.internet import task
from twisted.protocols import basic

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
	def __init__(self,name,fname,root):
		self.name = name
		self.fname = fname
		self.size = os.path.getsize(self.fname)
		
		self.info = {'name':name,'root':root,'size':self.size}

class Connection(basic.LineReceiver):
	def __init__(self, node):
		self.node = node
		self.state = 'GETHND'
		self.last_seen = time.time()
		self.download_position = 0
		self.is_downloader = False
		self.authed = False
		
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
		self.last_seen = time.time()

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
					elif self.node.info['security']=='open': self.sendLine('put::pwd::okay')
					
					self.authed = True
			
			elif line['opt']=='fie' and (self.authed or self.is_downloader):
				self.download_position = 0
			
			elif line['opt']=='png':
				self.last_seen = time.time()
			
			elif line['opt']=='bro' and self.node.info['broadcast'] and self.authed:
				_n = (self.host.host,self.host.port)
				
				if not _n in self.node.info['broadcasting']:
					self.node.info['broadcasting'].append(_n)
					self.node.log('[broadcast] Now broadcasting %s:%s' % _n)
					self.sendLine('put::bro::okay')
			
			#TODO: Document!
			elif line['opt']=='dwn':
				self.is_downloader=True
				
				self.sendLine('put::dwn::okay')
		
		elif line['com']=='get':
			if line['opt']=='inf' and self.authed:
				
				#Start our looping calls now.
				#Starts pinging clients
				self.ping_loop = task.LoopingCall(self.ping)
				self.ping_loop.start(10) #TODO: Make this a variable
				
				#TODO COMMENT: This might actually be a bad idea
				#If we did put this in, we'd have to tell the client
				#that the ping wouldn't be arriving at the expected time
				#and to hang on a bit longer before bailing out.
				
				#Sends a broadcast packet every <x> seconds
				#if self.node.info['broadcast']:
				self.broadcast_loop = task.LoopingCall(self.broadcast)
				self.broadcast_loop.start(self.node.info['broadcast_every'])
				
			elif line['opt']=='fil' and self.is_downloader:
				_f = self.node.get_file(line['val'])

				self.setRawMode()
				
				if self.download_position == 0:
					self.current_file = open(_f.fname,'rb')
				
				self.current_file.seek(self.download_position)
					
				byte = self.current_file.read(8100)
				
				self.download_position+=len(byte)
				
				if len(byte):
					self.transport.write(byte)
				else:
					self.download_position = 0
					self.current_file.close()
				
				self.setLineMode()
			
			elif line['opt']=='fli' and self.authed:
				if line['val']=='None':
					#If 'None', send our list of files down the pipe, in chunks of 32
					_cur = int(0)
					_max = _cur+32
					_done = False
					
					if _max>=len(self.node.file_list):
						_max=(len(self.node.file_list)-_cur)
						_done = True
					
					#TODO: Wut
					#if _cur==len(self.node.file_list):
					#	self.sendLine('put::fli::okay:%s' % self.node.info['file_list_version'])
					#	return
					
					_packet = []
					for f in range(_cur,_max):
						_packet.append(self.node.file_list[f])
					
					if len(_packet):
						self.sendLine('put::fli::%s' % (json.dumps(_packet)))
					
					if _done: self.sendLine('put::fli::okay:%s' % self.node.info['file_list_version'])
				else:
					print line['val']
					#print self.node.update_file_list(line['val'])
				
		else:
			print 'Garbage: '+str(line)

	def handle_PASSWORD(self, passwd):
		if not hashlib.sha224(passwd).hexdigest()==self.node.info['passwd']:
			self.sendLine('put::pwd::wrong')
			self.transport.loseConnection()
			return
		
		self.sendLine('put::pwd::okay')
		self.node.add_client((self.host.host,self.name))
	
	def handle_AUTH(self,usr,pas):
		if self.node.auth_user(usr,pas):
			self.sendLine('put::pwd::okay')
			self.node.add_client((self.host.host,self.name))
		else:
			self.sendLine('put::pwd::wrong')
			self.transport.loseConnection()
	
	def ping(self):
		self.sendLine('get::pin::null')
		
		if time.time()-self.last_seen > 30:
			self.transport.loseConnection()
	
	def broadcast(self):
		self.sendLine('put::inf::%s' % (json.dumps(self.node.info)))

class Node(ServerFactory):
	protocol = Connection

	def __init__(self,info,parent=None):
		self.info = info
		
		self.parent = parent
		
		self.clients = []
		self.connections = []
		
		self.files = []
		self.info['file_list_version'] = None
		self.file_lists = []
		self.populate_file_list()

	def log(self,text):
		if self.parent: self.parent.log(text)
		else: print text
	
	def stop(self):
		pass
	
	def populate_file_list(self):
		self.file_list = []
		
		for root, dirs, files in os.walk(self.info['share_dir']):
			for infile in files:
				_fname = os.path.join(root, infile)
				file, ext = os.path.splitext(_fname)
				
				if ext[1:] in self.info['ignore_filetypes']:
					continue
				
				_ignore = False
				for entry in self.info['ignore_filename']:
					if file.count(entry): _ignore = True
				
				if _ignore: continue
				
				if os.path.getsize(_fname):
					_f = File(infile,_fname,root.replace(self.info['share_dir'],''))
					
					self.files.append(_f)
					self.file_list.append(_f.info)
					#self.info['files'].append(_f.info)
		
		self.info['file_list_version'] = hashlib.sha224(str(self.file_list)).hexdigest()
		self.file_lists.append({'version':self.info['file_list_version'],'list':self.file_list[:]})
		
		self.log('[Files] Sharing %s files' % len(self.file_list))
	
	def update_file_list(self,version):
		for file_list in self.file_lists:
			if file_list['version']==version:
				return list(set(file_list['list'],self.file_list))
		
		return False
	
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
	def __init__(self,name='default',broadcast=False,searchable=False,network=None,parent=None,use_threading=True):
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
		self.info['ignore_filetypes'] = [s.encode('utf-8') for s in self.info['ignore_filetypes']]
		
		if self.info['security']=='auth':
			_adb = open(self.info['authdb'],'r')
			self.auth_db = json.loads(_adb.readline())
			_adb.close()
		
		if self.info['broadcast']:
			self.info['broadcasting'] = []
		
		if self.info.has_key('news_file') and os.path.exists(self.info['news_file']):
			self.info['news'] = ''
			_news = open(self.info['news_file'],'r')
			
			for line in _news.readlines():
				self.info['news']+=line
			
			_news.close()
		
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
			try:
				reactor.run(installSignalHandlers=0)
			except:
				self.log('[reactor.Warning] Client started reactor for us. How nice!')
		else:
			reactor.run()
	
	def stop(self):
		self.node.stop()
		reactor.stop()
		reactor.disconnectAll()
		
		self.running = False

if __name__ == "__main__":
	start_server(use_threading=False).start()
