#!/usr/bin/python
from __future__ import with_statement
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall

import hashlib, json, threading

class Client(Protocol):
	def __init__(self,host,parent):
		self.state = 'handshake'
		self.host = host
		self.parent = parent
		self.main_parent = self.parent.parent.parent
	
		self.file_data = ''
		
		self.main_parent.add_node_callback(self.host,self)
		
		self.pinging = False
	
	def stop(self):
		self.main_parent.remove_node(self.host)
		self.transport.loseConnection()
		self.parent.stop()

	def sendLine(self, line):
		self.transport.write(line+'\r\n')
	
	def connectionLost(self, reason):
		pass
		#self.stop()
	
	def ping(self):
		#self.sendLine('get::pin::null');
		self.sendLine('put::pin::%s:%s' % (self.host))
	
	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		if line.count('\r\n'): line = line[:len(line)-2]
		
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}
	
	def dataReceived(self, line):
		#print repr(line)
		
		#if not self.pinging:
		#	lc = LoopingCall(self.ping)
		#	lc.start(5)
		#	
		#	self.pinging = True
		
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
					_passwd = hashlib.sha224('derp').hexdigest()
					self.sendLine('put::pwd::'+_passwd)
					self.state = 'password'
				else:
					self.parent.log('[client->server] Server didn\'t like us. Abort.')
					self.stop()
					
			elif line['opt']=='pwd':
				if line['val']=='okay':
					self.parent.log('[client->server] Password accepted')
					self.sendLine('get::inf::%s' % self.parent.parent.parent.ip)
					self.state = 'running'
				else:
					self.parent.log('[client->server] Password incorrect. Abort.')
					self.stop()
					
			elif line['opt']=='inf':
				self.parent.info = json.loads(line['val'])
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
					self.main_parent.log('[client->%s] Grabbing file INSERT NAME HERE' % (self.parent.info['name']))
					self.state = 'grabbing'
				
				self.file_data+=line['val']
				self.sendLine('get::fil::helloworld.exe')
				
			elif line['opt']=='fie':
				_f = open('test.exe','wb')
				_f.write(self.file_data)
				_f.close()
				
				self.main_parent.log('[client->%s] Grabbed file INSERT NAME HERE' % (self.parent.info['name']))
				
				self.state = 'running'
			
			elif line['opt']=='fib':
				self.main_parent.log('[client->%s] Failed grabbing file INSERT NAME HERE' % (self.parent.info['name']))
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
	
	def startedConnecting(self, connector):
		#self.log('[client->server] Connecting...')
		pass

	def buildProtocol(self, addr):	
		#self.log('[client->server] Connected')
		_c = Client(self.host,self)
		self.connections.append(_c)
		return _c

	def clientConnectionLost(self, connector, reason):
		print 'Lost connection.  Reason:', reason

	def clientConnectionFailed(self, connector, reason):
		print 'Connection failed. Reason:', reason
	
class connect(threading.Thread):
	def __init__(self,parent):
		#self.host = host
		self.parent = parent
		self.ClientParent = None
		
		self.running = False

		threading.Thread.__init__(self)
	
	def stop(self):
		if self.ClientParent: self.ClientParent.stop()
		self.running = False
	
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

		if not self.running: self.start()

#point = TCP4ClientEndpoint(reactor, 'localhost', 9001)
#point.connect(ClientParent(reactor))
#reactor.run()
