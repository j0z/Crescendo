#!/usr/bin/python
from __future__ import with_statement
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall

import hashlib, json, threading

class File:
	def __init__(self,name,fname):
		self.name = name
		self.fname = fname
		self.fpos = 0
		self.data = ''

class Client(Protocol):
	def __init__(self,host,parent):
		self.state = 'handshake'
		self.host = host
		self.parent = parent
		self.file = None
		self.main_parent = self.parent.parent.parent
		self.main_parent.add_node_callback(self.host,self)
	
	def stop(self):
		self.main_parent.remove_node(self.host)
		self.transport.loseConnection()
		#self.parent.stop()
	
	def get_file(self,file):
		self.getting_file = file
		self.sendLine('get::fil::%s' % str(self.getting_file))

	def sendLine(self, line):
		self.transport.write(line+'\r\n')
	
	def connectionLost(self, reason):
		pass
	
	def ping(self):
		#self.sendLine('get::pin::null');
		self.sendLine('put::pin::%s:%s' % (self.host))
	
	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		if line.count('\r\n'): line = line[:len(line)-2]
		
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}
	
	def dataReceived(self, line):
		#print repr(line)
		
		if line.count('\r\n')>=2:
			for _l in line.split('\r\n'):
				self.parse_data(self.parse_line(_l))
		else: self.parse_data(self.parse_line(line))
	
	def parse_data(self,line):
		if line['com']=='get':
			if line['opt']=='hnd':
				self.sendLine('put::hnd::%s' % self.parent.name)
					
		elif line['com']=='put':
			if line['opt']=='hnd':
				if line['val']=='okay':
					self.parent.log('[client->server] Handshake accepted')
					
					#This needs to be done serverside
					#_passwd = hashlib.sha224('derp').hexdigest()
					self.sendLine('put::pwd::derp')
					self.state = 'password'
				else:
					self.parent.log('[client->server] Server didn\'t like us. Abort.')
					self.stop()
					
			elif line['opt']=='pwd':
				if line['val']=='okay':
					self.parent.log('[client->server] Password accepted')
					self.sendLine('get::inf::derp')
					self.state = 'running'
				else:
					self.parent.log('[client->server] Password incorrect. Abort.')
					self.stop()
					
			elif line['opt']=='inf':
				self.parent.info = json.loads(line['val'])
				self.parent.info['host'] = self.host
				self.main_parent.add_node_info(self.host,self.parent.info)
				
				#lol
				#if self.parent.parent.parent.server.running:
				#	#if not self.parent.parent.parent.has_node(self.host):
				#	#if self.parent.parent.parent.server.node.host == self.host: print 'YES'
				#	#self.sendLine('put::con::%s:%s' % (self.host))
				#
				#self.sendLine('get::fil::helloworld.exe')
				
			elif line['opt']=='fil':
				if not self.state=='grabbing':
					self.main_parent.log('[client->%s] Grabbing file %s' % (self.parent.info['name'],self.getting_file))
					self.file = File(self.getting_file,self.getting_file)
					
					self.state = 'grabbing'
				
				self.file.data+=line['val']
				self.sendLine('get::fil::%s' % str(self.getting_file))
				
			elif line['opt']=='fie':
				if not len(self.data):
					self.main_parent.log('[client->%s] File \'%s\' was empty.' % (self.parent.info['name'],self.getting_file))
				_f = open(self.getting_file,'wb')
				_f.write(self.file.data)
				_f.close()
				
				self.main_parent.log('[client->%s] Grabbed file \'%s\'' % (self.parent.info['name'],self.getting_file))
				
				self.state = 'running'
			
			elif line['opt']=='fib':
				self.main_parent.log('[client->%s] Failed grabbing file \'%s\'' % (self.parent.info['name'],self.getting_file))
				self.state = 'running'
			
				#elif line['opt']=='pin':
				#self.sendLine('put::pin::%s:%s' % (self.host))
				
			elif line['opt']=='kil':
				self.main_parent.log('[client->%s] Server is dying. Disconnecting' % self.parent.info['name'])
				self.stop()
		
class ClientParent(ClientFactory):
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
			print client.host[0],host
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
