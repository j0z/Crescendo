#!/usr/bin/python
import sys, hashlib, json
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Connection(LineReceiver):
	def __init__(self, node):
		#self.users = users
		self.node = node
		self.state = 'GETHND'
		
		self.name = ''

	def connectionMade(self):
		self.sendLine('get::hnd::null')
		self.host = self.transport.getHost()

	def connectionLost(self, reason):
		pass

	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}
	
	def lineReceived(self, line):
		line = self.parse_line(line)
		
		if line['com']=='put':
			if line['opt']=='hnd':
				#Shake hands if we haven't already.
				if self.state=='GETHND':
					self.sendLine('put::hnd::okay')
					self.name = line['val']
					self.state='GETPASSWD'
				else:
					self.sendLine('put::hnd::Already shook hands!')
			elif line['opt']=='pwd':
				if self.state=='GETPASSWD': self.handle_GETPASSWD(line['val'])
		elif line['com']=='get':
			if line['opt']=='inf':
				self.sendLine('put::inf::%s' % (json.dumps(self.node.get_info())))

	def handle_GETPASSWD(self, passwd):
		if not passwd==self.node.passwd:
			self.sendLine('put::pwd::wrong')
			return
		
		self.sendLine('put::pwd::okay')
		self.node.add_client('%s:%s' % (self.host.host,self.name))
		self.state = "GET"

class Node(Factory):
	def __init__(self,name='default',searchable=False,network=None,passwd=None):
		self.name=name
		self.passwd = passwd
		self.searchable = searchable
		self.network = network
		self.clients = []

	def log(self,text):
		print text
		
	def has_client(self,who):
		for client in self.clients:
			if client['name']==who: return True
		
		return False
	
	def add_client(self,who):
		if not self.has_client(who):
			self.clients.append({'name':who})
			self.log('[client.Added] %s' % who)

	def get_info(self):
		return {'name':self.name,'searchable':self.searchable,'network':self.network,'clients':len(self.clients)}
	
	def buildProtocol(self, addr):
		self.log('[client.New] %s:%s' % (addr.host,addr.port))
		return Connection(self)

if len(sys.argv)==2 and sys.argv[1]=='runserver':
	reactor.listenTCP(9001, Node(passwd='22c7d75bd36e271adc1ef873aee4f95db6bc54a9c2f9f4bcf0cd18a8'))
	reactor.run()
