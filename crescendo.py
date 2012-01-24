#/usr/bin/python
import subprocess
import crescendo_server as server
import crescendo_search as search
import crescendo_client as client

class crescendo:
	def __init__(self):
		self.node_list = []
		
		self.running = True		

	def log(self,text):
		print text
	
	def start_server(self):
		#server.
		pass

	def populate_node_list(self):
		self.log('[search.Engine] Running search.Engine')
		try:
			_s = search.Engine(self)
			_s.start()
			self.log('[search.Engine] Search invoked and starting')
		except:
			self.log('[search.Engine] Failed.')
			return False
		
		#while _s.is_running(): pass
		
		#if _s.has_clients():
		#	self.client_list = _s.get_clients()
		#	self.log('[search.Engine] Found: %s' % len(self.client_list))
		#else:
		#	self.log('[search.Engine] No clients found')
	
	def connect_node_list(self):
		for node in self.node_list:
			if not node['connected']:
				_c = client.connect(node['host'],self)
				_c.start()
				
				node['connected']=True
				
				self.log('[node] Connecting to %s:%s' % node['host'])
	
	def disconnect_node_list(self):
		for node in self.node_list:
			if node['connected']:
				self.log('[node-%s:%s] Disconnecting...' % node['host'])
				node['callback'].stop()
	
	def add_node(self,host):
		self.node_list.append({'host':host,'connected':False})
		self.log('[node] Found node at %s:%s' % (host))
	
	def add_node_callback(self,host,obj):
		for node in self.node_list:
			if node['host']==host:
				node['callback']=obj
	
	def tick(self):
		while self.running:
			try:
				self.connect_node_list()
			except KeyboardInterrupt:
				self.log('[crescendo] KeyboardInterrupt caught')
				self.log('[crescendo] Killing node connections')
				self.disconnect_node_list()
				
				self.running = False

_c = crescendo()
_c.populate_node_list()
_c.tick()
