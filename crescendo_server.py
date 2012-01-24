#!/usr/bin/python
import sys, hashlib
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):
	def __init__(self, passwd):
		#self.users = users
		self.passwd = passwd
		self.state = 'GETPASSWD'

	def connectionMade(self):
		self.sendLine('Password?')

	def connectionLost(self, reason):
		pass
		#if self.users.has_key(self.name):
		#	del self.users[self.name]

	def lineReceived(self, line):
		#print repr(line)
		if self.state == 'GETPASSWD':
			self.handle_GETPASSWD(line)
		else:
			self.handle_CHAT(line)

	def handle_GETPASSWD(self, passwd):
		print repr(passwd)
		if not passwd==self.passwd:
			self.sendLine('Wrong.')
			return
		print 'RIGHT'
		self.sendLine('Welcome')
		self.state = "CHAT"

	def handle_CHAT(self, message):
		message = "<%s> %s" % (self.name, message)
		for name, protocol in self.users.iteritems():
			if protocol != self:
				protocol.sendLine(message)


class ChatFactory(Factory):
	def __init__(self):
		self.passwd = '22c7d75bd36e271adc1ef873aee4f95db6bc54a9c2f9f4bcf0cd18a8' 

	def log(self,text):
		print text

	def buildProtocol(self, addr):
		print '[client.New] %s' % addr
		return Chat(self.passwd)

if len(sys.argv)==2 and sys.argv[1]=='runserver':
	reactor.listenTCP(9001, ChatFactory())
	reactor.run()
