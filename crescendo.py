#/usr/bin/python
import subprocess
import crescendo_server as server
import crescendo_search as search
import crescendo_client as client

class crescendo:
	def __init__(self,callback=None):
		self.callback = callback
		
		self.node_list = []
		
		self.wanted_files = []
		self.shared_files = []
		
		self._log = []
	
		self.client = client.connect(self)
		self.server = server.start_server()
		
		self.running = True
	
	def start_server(self):
		self.log('[server] Starting server...')
		self.server.start()

	def log(self,text,flush=False):
		if flush: print text
		else: self._log.append(text)
	
	def print_log(self):
		while (len(self._log)):
			print self._log.pop(0)

	def populate_node_list(self):
		self.log('[search.Engine] Running search.Engine')
		try:
			_s = search.Engine(self)
			_s.start()
			self.log('[search.Engine] Search invoked and starting')
		except:
			self.log('[search.Engine] Failed.')
			return False
	
	def connect_node_list(self):
		for node in self.node_list:
			if not node['connected']:
				self.client.add_client(node['host'])

				node['connected']=True
				
				self.log('[node] Connecting to %s:%s' % node['host'])
	
	def disconnect_node_list(self):
		for node in self.node_list:
			if node['connected']:
				if node.has_key('info'):
					self.log('[node-%s] Disconnecting...' % node['info']['name'],flush=True)
				else:
					self.log('[node-%s:%s] Disconnecting...' % node['host'],flush=True)
				
				if node.has_key('callback'):
					node['callback'].stop()
				else:
					self.log('[node-%s:%s] Connection is a zombie. Dying' % node['host'],flush=True)
	
	def has_node(self,host):
		for node in self.node_list:
			if node['host']==host: return True
		
		return False
	
	def add_node(self,host):
		self.node_list.append({'host':host,'connected':False})
		self.log('[node] Found node at %s:%s' % (host))
		
		if self.callback:
			self.callback.add_node(host[0])
	
	def remove_node(self,host):
		for node in self.node_list:
			if node['host']==host:
				self.node_list.remove(node)
				
				#self.log('[node-%s] Disconnecting' % node['info']['name'])
	
	def add_node_callback(self,host,obj):
		for node in self.node_list:
			if node['host']==host:
				node['callback']=obj
	
	def add_node_info(self,host,info):
		for node in self.node_list:
			if node['host']==host:
				node['info']=info
				self.log('[node.Info.name] %s -> %s ' % (node['host'][0],node['info']['name']),flush=True)
	
	def shutdown(self):
		if self.client.running:
			self.log('[crescendo] Stopping client...',flush=True)
		
		self.client.stop()
		
		#try:
		self.server.stop()
		#except:
		#	pass
		
		if len(self.node_list):
			self.log('[crescendo] Killing node connections',flush=True)
			self.disconnect_node_list()
		else: self.log('[crescendo] No node connections to kill',flush=True)
		
		self.running = False
	
	def tick(self):
		try:	
			while self.running:
				self.connect_node_list()
				if len(self._log): print self._log.pop(0)
		except KeyboardInterrupt:
			self.running = False
		
		self.shutdown()

if __name__ == "__main__":
	_c = crescendo()
	_c.populate_node_list()
	_c.start_server()
	_c.tick()
