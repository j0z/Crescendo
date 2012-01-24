#!/usr/bin/python
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from sys import stdout
import hashlib

class Client(Protocol):
	def __init__(self,factory):
		self.state = 'handshake'
		self.factory = factory

	def dataReceived(self, data):
		#print repr(data)
		if self.state=='handshake':
			_passwd = hashlib.sha224('derp').hexdigest()
			self.transport.write(_passwd+'\r\n')
			#print 'sent derp'
			self.state='login'
		else:
			if data=='Welcome\r\n':
				self.factory.log('[client->server] Password accepted.')
				self.transport.write('Give me a file!')
			else:
				print repr(data)
				self.factory.log('[client->server] Password incorrect.')

class ClientFactory(ClientFactory):
	def log(self, text):
		print text
	
	def startedConnecting(self, connector):
		self.log('[client->server] Connecting...')

	def buildProtocol(self, addr):	
		self.log('[client->server] Connected')
		return Client(self)

	def clientConnectionLost(self, connector, reason):
		print 'Lost connection.  Reason:', reason
		connector.connect()

	def clientConnectionFailed(self, connector, reason):
		print 'Connection failed. Reason:', reason

point = TCP4ClientEndpoint(reactor, "localhost", 9001)
d = point.connect(ClientFactory())
#d.addCallback(gotProtocol)
reactor.run()
