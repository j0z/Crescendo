#!/usr/bin/python
from __future__ import with_statement
from twisted.internet import reactor, defer
from twisted.internet.protocol import Protocol, ClientFactory, ReconnectingClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import task
from twisted.protocols import basic

import os, time, json, threading

class File:
	def __init__(self,name,fname,total_size,save_dir='downloads'):
		self.name = name
		self.fname = fname
		self.size = 0
		self.total_size = total_size
		self.save_dir = save_dir
		
		self.fpos = 0
		self.data = ''
		self.done = False
		
		self.info = {'name':name,'fname':fname,'size':self.total_size}
		
		try:
			os.mkdir(self.save_dir)
			print '[crescendo] Created folder'
		except:
			pass
	
		self.f = open(os.path.join(self.save_dir,self.name),'wb')
	
	def compress(self):
		pass
	
	def get_size(self):
		return os.path.getsize(os.path.join(self.save_dir,self.name))
	
	def is_done(self):
		if self.size>=self.total_size:
			return True
		
		return False
	
	def write(self,text):
		self.size+=len(text)
		self.f.write(text)
	
	def close(self):
		self.f.close()

class Client(basic.LineReceiver):
	def __init__(self,host,parent):
		self.state = 'handshake'
		self.host = host
		self.parent = parent
		self.file = None
		self.main_parent = self.parent.parent.parent
		self.main_parent.add_node_callback(self.host,self)
		
		self.ping_loop = task.LoopingCall(self.ping)
		
		self.last_seen = time.time()
		
		self.file_list_temp = []
	
	def stop(self):
		self.main_parent.remove_node(self.host)
		self.transport.unregisterProducer()
		self.transport.stopConsuming()
		self.transport.loseConnection()
		try:
			self.ping_loop.stop()
		except:
			pass
	
	def get_file(self,file):
		self.getting_file = str(file)
		
		try:
			self.ping_loop.stop()
		except:
			pass
		
		#TODO: File resuming
		self.sendLine('get::fil::%s' % (self.getting_file))
		
		self.main_parent.log('[client->%s] Grabbing file %s' % (self.parent.info['name'],self.getting_file))
		self.file = File(self.getting_file,self.getting_file,self.get_file_info(self.getting_file,'size'),save_dir=self.main_parent.info['save_dir'])
		self.main_parent.wanted_files.append(self.getting_file)
						
		self.setRawMode()
	
	def get_file_info(self,name,info):
		for f in self.parent.info['files']:
			if f['name']==name:
				return f[info]
		
		return False

	def sendLine(self, line):
		self.transport.write(str(line)+'\r\n')
	
	def connectionMade(self): 
		print 'CONNECTION MADE'
	
	def connectionLost(self, reason):
		print '[Failure] Client is shutting down for some reason'
		print reason
		#self.parent.restart()
	
	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		if line.count('\r\n\r\n'): line = line[:len(line)-4]
		
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}
	
	def lineReceived(self, line):
		self.last_seen = time.time()
		#print repr(line)
		
		if line.count('\r\n\r\n')>=2:
			for _l in line.split('\r\n\r\n'):
				self.parse_data(self.parse_line(_l))
		else:
			_l = self.parse_line(line)
			
			if not _l['com'] in ['put','get']:
				_l = {'com':'put','opt':'fil','val':line}
			
			self.parse_data(_l)
	
	def rawDataReceived(self, data):
		self.last_seen = time.time()
		
		self.file.write(data)
		
		self.main_parent.set_download_progress(self.file.get_size(),self.file.info)
		self.setLineMode()
		
		if self.file.is_done():
			self.main_parent.log('[client->%s] Grabbed file %s' % (self.parent.info['name'],self.getting_file))
			self.sendLine('put::fie::okay')
			self.ping_loop.start(10)
			self.file.close()
			self.main_parent.set_download_progress(self.file.info['size'],self.file.info)
			print '[services] Restarted'
		else:
			self.sendLine('get::fil::%s' % (self.getting_file))
			self.setRawMode()
	
	def parse_data(self,line):
		if line['com']=='get':
			if line['opt']=='hnd':
				self.sendLine('put::hnd::%s' % self.parent.name)
			
			elif line['opt']=='pin':
				if self.parent.info:
					#self.main_parent.log('[node.%s] Ping' % (self.parent.info['name']))
					self.last_seen = time.time()
					self.sendLine('put::png::null')
					
		elif line['com']=='put':
			if line['opt']=='hnd':
				if not line['val']=='error':
					self.parent.log('[client->server] Handshake accepted')
					
					#Here we identify what login method the node/network uses
					if line['val']=='auth':
						#Handle auth by reading from the profile associated with this node
						self.sendLine('put::pwd::test:test')
					else:
						self.sendLine('put::pwd::derp')
					self.state = 'password'
				else:
					self.parent.log('[client->server] Server didn\'t like us. Abort.')
					self.stop()
					
			elif line['opt']=='pwd':
				if line['val']=='okay':
					self.parent.log('[client->server] Password accepted')
					
					#We start our loops now
					self.ping_loop.start(10)
					
					self.sendLine('get::inf::derp')
					self.state = 'running'
				else:
					self.parent.log('[client->server] Password incorrect. Abort.')
					self.stop()
			
			elif line['opt']=='inf':
			
				#We grab the total number of nodes being broadcasted and compare
				#them to the amount that were in the last info packet to the info
				#packet received a few lines down.
				_nodes=None
				if self.parent.info and self.parent.info.has_key('broadcasting'):
					_nodes = str(len(self.parent.info['broadcasting']))
				
				#Get the info packet and run it through json
				#try:
				self.parent.info = json.loads(line['val'])
				self.parent.info['host'] = self.host
				self.parent.info['files'] = self.file_list_temp
				self.main_parent.add_node_info(self.host,self.parent.info)
				#except:
				#	pass
				
				#If broadcast node, handle it accordingly
				#TODO: Some clients might not want to listen to broadcasts...
				if self.parent.info['broadcast']:
					if not _nodes == str(len(self.parent.info['broadcasting'])):
						self.main_parent.log('[node.%s] Broadcasting %s nodes' % (self.parent.info['name'],str(len(self.parent.info['broadcasting']))))
					
					#Here we do some work for the node running on the local machine
					#However, since we can't talk directly to it to see if it's running,
					#we have to work in a few hacks. 
					#Check if we even need to do this first.
					#TODO: There might be an error here, but I'm not sure.
					#	Basically we're cheating and reading in the node's config file even though a node
					#	is not running.
					#	For now it works because the node config is read when we create self.server
					#	in crescendo.py. When the config file format changes we'll need to edit this.
					if self.main_parent.server.info['searchable'] and self.main_parent.has_node(('127.0.0.1',9001)):
						self.sendLine('put::bro::%s:%s' % (self.main_parent.info['host']))
					
					#I would like to add some kind of message here if the node was added
					#or not... just so the user can know that they are getting nodes
					#from a broadcast node.
					for node in self.parent.info['broadcasting']:
						if not str(node[0]) == self.main_parent.info['host'][0]:
							self.main_parent.add_node((str(node[0]),int(node[1])))
				
				#Finally, we let the node know that we need its file listing
				#TODO: Check to see if the size of our list is the size of the node's list
				if not len(self.file_list_temp):
					self.sendLine('get::fli::0')
			
			elif line['opt']=='fli':
				if line['val']=='okay':
					self.parent.info['files'] = self.file_list_temp[:]
				else:
					_tlist = json.loads(line['val'])
					for entry in _tlist:
						self.file_list_temp.append(entry)
					
					self.sendLine('get::fli::%s' % len(self.file_list_temp))
			
			elif line['opt']=='fib':
				self.main_parent.log('[client->%s] Failed grabbing file \'%s\'' % (self.parent.info['name'],self.getting_file))
				self.state = 'running'
				
			elif line['opt']=='kil':
				self.main_parent.log('[client->%s] Server is dying. Disconnecting' % self.parent.info['name'])
				self.stop()
			
			#TODO: WE NEED TO CHECK IF WE ARE LOGGED IN.
			if line['opt']=='bro':
				self.main_parent.log('[node.%s->node.%s] Added ourself to broadcast' % (self.main_parent.server.info['name'],self.parent.info['name']))
		else:
			print line
			pass
			#if str(line).count('<crlf>'):
			#a = open('debug','ab')
			#a.write(str(line)+'\n')
			#a.close()
			#print 'Had to throw a line out: %s!!!' % str(line)
	def ping(self):
		if time.time()-self.last_seen >= 30:
			self.main_parent.log('[client->%s] Connection lost' % self.parent.info['name'])
			self.stop()
		
class ClientParent(ClientFactory):
	protocol = Client

	def __init__(self,host,parent,name='Unnamed'):
		self.host = host
		self.parent = parent
		self.name = name
		self.connections = []
		self.info = None
		
		self.debug = True
	
	def log(self, text):
		if self.debug: self.parent.parent.log(text)
	
	def stop(self):
		try:
			self.parent.reactor.stop()
		except:
			self.log('[client.Failure] Parent reactor already stopped')
		
		for con in self.connections:
			con.transport.loseConnection()
		
		self.parent.clients.remove(self)
	
	def get_file(self,file):
		self.client.get_file(file)
	
	def startedConnecting(self, connector):
		#self.log('[client->server] Connecting...')
		pass

	def buildProtocol(self, addr):
		#self.log('[client->server] Connected')
		_c = Client(self.host,self)
		self.connections.append(_c)
		self.client = _c
		return _c
	
	def clientConnectionLost(self, connector, reason):
		print 'Lost connection.  Reason:', reason
		ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

	def clientConnectionFailed(self, connector, reason):
		print 'Connection failed. Reason:', reason
	
class connect(threading.Thread):
	def __init__(self,parent):
		#self.host = host
		self.parent = parent
		self.clients = []
		self.ClientParent = None
		
		self.running = False

		threading.Thread.__init__(self)
	
	def stop(self):
		if self.ClientParent: self.ClientParent.stop()
		self.running = False
	
	def get_file(self,host,file):
		_c = self.get_client(host)
		
		if _c:
			_c.get_file(file)
	
	def get_client(self,host):
		for client in self.clients:
			if client.host[0]==host:
				return client
		
		self.parent.log('[client.Failure] Client %s does not exist!' % (host))
		
		return False
	
	def run(self):
		self.running = True
		self.reactor = reactor
		
		try:
			reactor.run(installSignalHandlers=0)
		except:
			pass

	def add_client(self,host):	
		self.point = TCP4ClientEndpoint(reactor, host[0], host[1])
		self.ClientParent = ClientParent(host,self)
		self.point.connect(self.ClientParent)
		
		self.clients.append(self.ClientParent)

		if not self.running: self.start()

#point = TCP4ClientEndpoint(reactor, 'localhost', 9001)
#point.connect(ClientParent(reactor))
#reactor.run()
