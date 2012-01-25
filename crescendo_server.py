#!/usr/bin/python
import os, hashlib, json
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class File:
	def __init__(self,name,fname):
		self.name = name
		self.fname = fname
		self.fpos = 0

class Connection(LineReceiver):
	def __init__(self, node):
		#self.users = users
		self.node = node
		self.state = 'GETHND'
		self.file_pos = 0
		
		self.name = ''

	def connectionMade(self):
		self.sendLine('get::hnd::null')
		self.host = self.transport.getHost()

		#def stop(self):
		#self.sendLine('put::kil::sorry')
		#self.transport.loseConnection()

	def connectionLost(self, reason):
		self.node.connections.remove(self)
		self.node.remove_client((self.host.host,self.name))
	
		if self.state=='GETHND': return
		
		if self.name: self.node.log('[client-%s] Disconnected' % (self.name))
		else: self.node.log('[client-%s] Disconnected' % (self.host.host))

	def parse_line(self, line):
		#Server expects a line similar to: GET/PUT::OPT::VAL
		return {'com':line[:3],'opt':line[5:8],'val':line[10:]}
	
	def lineReceived(self, line):
		line = self.parse_line(line)
		#print line

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
				
			elif line['opt']=='fil':
				_f = self.node.get_file(line['val'])
				
				if not _f:
					self.sendLine('put::fib::error')
					return
				
				if not _f.fpos: self.node.log('[client-%s] Getting file: %s' % (self.name,_f.name))
				
				with open(_f.fname, "rb") as f:
					f.seek(_f.fpos)
					byte = f.read(6)
					_f.fpos+=len(byte)
					
					if byte != b"":
						self.sendLine('put::fil::%s' % byte)
					else:
						self.sendLine('put::fie::end')
						self.node.log('[client-%s] Got file: %s' % (self.name,_f.name))

	def handle_GETPASSWD(self, passwd):
		if not passwd==self.node.passwd:
			self.sendLine('put::pwd::wrong')
			return
		
		self.sendLine('put::pwd::okay')
		self.node.add_client((self.host.host,self.name))
		self.state = "GET"

class Node(Factory):
	def __init__(self,parent,name,searchable,network,passwd):
		self.parent = parent
		self.name = name
		self.passwd = passwd
		self.searchable = searchable
		self.network = network
		self.clients = []
		self.connections = []
		self.files = []
		
		self.populate_file_list()

	def log(self,text):
		self.parent.log(text)
	
	def populate_file_list(self):
		for root, dirs, files in os.walk('files'):
			for infile in files:
				_fname = os.path.join(root, infile)
				file, ext = os.path.splitext(_fname)
				
				self.files.append(File(infile,_fname))
				if ext in ['.exe','.JPG','.png','.PNG']:
					pass
	
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

	def get_info(self):
		return {'name':self.name,'searchable':self.searchable,'network':self.network,'clients':len(self.clients)}
	
	def buildProtocol(self, addr):
		_c = Connection(self)
		self.connections.append(_c)
		
		return _c

class start_server:
	def __init__(self,parent,name='default',searchable=False,network=None,passwd='22c7d75bd36e271adc1ef873aee4f95db6bc54a9c2f9f4bcf0cd18a8'):
		self.parent = parent
		
		self.name = name
		self.passwd = passwd
		self.searchable = searchable
		self.network = network
	
	def start(self):
		_n = Node(self.parent,name=self.name,passwd=self.passwd,searchable=self.searchable,network=self.network)
		reactor.listenTCP(9001, _n)