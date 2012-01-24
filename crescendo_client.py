#!/usr/bin/python
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from sys import stdout
import hashlib, json, threading

class Client(Protocol):
	def __init__(self,parent):
		self.state = 'handshake'
		self.parent = parent
		
		self.parent.parent.parent.add_node_callback(self.parent.parent.host,self)
	
	def stop(self):
		self.transport.loseConnection()
		self.parent.stop()
	
	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		line = line[:len(line)-2]
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}

	def sendLine(self, line):
		self.transport.write(line+'\r\n')
	

	def dataReceived(self, line):
		line = self.parse_line(line)
		#print repr(line)
		
		if line['com']=='get':
			if line['opt']=='hnd':
				self.sendLine('put::hnd::%s' % self.parent.name)
			#elif line['opt']=='pwd':
			#	if line['val']=='okay':
					
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
					self.transport.loseConnection()
			elif line['opt']=='pwd':
				if line['val']=='okay':
					self.parent.log('[client->server] Password accepted')
					self.sendLine('get::inf::null')
				else:
					self.parent.log('[client->server] Password incorrect. Abort.')
					self.transport.loseConnection()
			elif line['opt']=='inf':
				self.parent.info = json.loads(line['val'])
		
class ClientParent(ClientFactory):
	def __init__(self,parent):
		self.parent = parent
		self.name = 'testconnection'
		
		self.info = None
		
		self.debug = False
	
	def log(self, text):
		if self.debug: print text
	
	def has_info(self):
		if self.info: return True
		else: return False
	
	def get_info(self):
		return self.info()
		#print 'NAME:\t\t%s' % _info['name']
		#print 'CLIENTS:\t%s' % _info['clients']
	
	def stop(self):
		self.parent.reactor.stop()
	
	def startedConnecting(self, connector):
		#self.log('[client->server] Connecting...')
		pass

	def buildProtocol(self, addr):	
		#self.log('[client->server] Connected')
		return Client(self)

	def clientConnectionLost(self, connector, reason):
		print 'Lost connection.  Reason:', reason

	def clientConnectionFailed(self, connector, reason):
		print 'Connection failed. Reason:', reason
	
class connect(threading.Thread):
	def __init__(self,host,parent):
		self.host = host
		self.parent = parent
		
		threading.Thread.__init__(self)
	
	def run(self):
		point = TCP4ClientEndpoint(reactor, self.host[0], self.host[1])
		self.reactor = reactor
		point.connect(ClientParent(self))
		reactor.run(installSignalHandlers=0)

#point = TCP4ClientEndpoint(reactor, 'localhost', 9001)
#point.connect(ClientParent(reactor))
#reactor.run()
