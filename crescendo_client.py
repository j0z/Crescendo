#!/usr/bin/python
from __future__ import with_statement
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from sys import stdout
import hashlib, json, threading

class Client(Protocol):
	def __init__(self,host,parent):
		self.state = 'handshake'
		self.host = host
		self.parent = parent
		self.main_parent = self.parent.parent.parent
	
		self.file_data = ''
		
		self.main_parent.add_node_callback(self.host,self)
	
	def stop(self):
		self.main_parent.remove_node(self.host)
		self.transport.loseConnection()
		self.parent.stop()
	
	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		line = line[:len(line)-2]
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}

	def sendLine(self, line):
		self.transport.write(line+'\r\n')
	
	def connectionLost(self, reason):
		self.stop()
	
	def dataReceived(self, line):
		line = self.parse_line(line)
		print repr(line)
		
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
					self.sendLine('get::inf::null')
					self.state = 'running'
				else:
					self.parent.log('[client->server] Password incorrect. Abort.')
					self.stop()
					
			elif line['opt']=='inf':
				self.parent.info = json.loads(line['val'])
				self.main_parent.add_node_info(self.host,self.parent.info)
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
				
			elif line['opt']=='kil':
				self.main_parent.log('[client->%s] Server is dying. Disconnecting' % self.parent.info['name'])
				self.stop()
		
class ClientParent(ClientFactory):
	def __init__(self,host,parent,name='Unnamed'):
		self.host = host
		self.parent = parent
		self.name = name
		
		self.info = None
		
		self.debug = False
	
	def log(self, text):
		if self.debug: self.parent.parent.log(text)
	
	def stop(self):
		try:
			self.parent.reactor.stop()
		except:
			self.log('[client.Failure] Parent reactor already stopped')
	
	def startedConnecting(self, connector):
		#self.log('[client->server] Connecting...')
		pass

	def buildProtocol(self, addr):	
		#self.log('[client->server] Connected')
		return Client(self.host,self)

	def clientConnectionLost(self, connector, reason):
		print 'Lost connection.  Reason:', reason

	def clientConnectionFailed(self, connector, reason):
		print 'Connection failed. Reason:', reason
	
class connect(threading.Thread):
	def __init__(self,parent):
		#self.host = host
		self.parent = parent
		
		self.running = False

		threading.Thread.__init__(self)
	
	def run(self):
		self.running=True
		#self.point = TCP4ClientEndpoint(reactor, self.host[0], self.host[1])
		self.reactor = reactor
		#self.point.connect(ClientParent(self))
		try:
			reactor.run(installSignalHandlers=0)
		except:
			pass

	def add_client(self,host):	
		self.point = TCP4ClientEndpoint(reactor, host[0], host[1])
		self.point.connect(ClientParent(host,self))

		if not self.running: self.start()

#point = TCP4ClientEndpoint(reactor, 'localhost', 9001)
#point.connect(ClientParent(reactor))
#reactor.run()
