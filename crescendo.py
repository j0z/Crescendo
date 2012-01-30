#/usr/bin/python
import subprocess, json, threading, sys
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
		
		_temp_info = ''
		
		_f = open('config.conf','r')
		for line in _f.readlines():
			_temp_info += line.replace('\n','')
		_f.close()
		
		self.info = json.loads(_temp_info)
		self.info['host'] = tuple(self.info['host'])
		
		self.ip_list = ['127.0.0.1','10.234.16.10']
		
		self.client = client.connect(self)
		self.server = server.start_server(parent=self)
		self.search = search.Engine(self,ip_list=self.ip_list)
		
		self.can_search = False
		self.running = True
	
	def start_server(self):
		self.log('[server] Starting server...')
		self.server.start()
	
	def start_client(self):
		self.log('[server] Starting client...')
		self.client.start()
	
	def search_done(self):
		self.can_search = True
		
		_ip_list = self.ip_list[:]
		for ip in self.ip_list:
			if self.has_node([ip]):
				_ip_list.remove(ip)
		
		self.search = search.Engine(self,ip_list=_ip_list)

	def log(self,text,flush=False):
		if flush: print text
		else: self._log.append(text)
		
		if self.callback:
			self.callback.log(text)

	def populate_node_list(self):
		#self.log('[search.Engine] Running search.Engine')
		
		#try:
		self.can_search = False
		self.search.start()
		#self.log('[search.Engine] Search invoked and starting')
		#except:
		#	self.log('[search.Engine] Failed.')
		#	return False
	
	def connect_node_list(self):
		for node in self.node_list:
			if not node['connected']:
				#print node['host']
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
			if node['host'][0]==host[0]: return True
		
		return False
	
	def add_node(self,host):
		if not self.has_node(host):
			self.node_list.append({'host':host,'connected':False})
			self.log('[node] Found node at %s:%s' % (host))
		
			if self.callback:
				self.callback.add_node(host[0])
	
	def remove_node(self,host):
		for node in self.node_list:
			if node['host']==host:
				if self.callback:
					self.callback.remove_node(self.get_node_info(host)['name'])
				
				self.node_list.remove(node)
	
	def add_node_callback(self,host,obj):
		for node in self.node_list:
			if node['host']==host:
				node['callback']=obj
	
	def add_node_info(self,host,info):
		for node in self.node_list:
			if node['host']==host:
				_oname = None
				if node.has_key('info'):
					_oname = node['info']['name']
				
				node['info']=info
				if not node['info']['name']==_oname:
					self.log('[node.Info.name] %s -> %s ' % (node['host'][0],node['info']['name']),flush=True)
				
				if self.callback:
					self.callback.update_node(node['host'][0],node['info'])
	
	def get_node_info(self,host):
		for node in self.node_list:
			if str(node['host'][0])==host[0]:
				return node['info']
		
		return False
	
	def get_file(self,host,file):
		self.client.get_file(host,file)
	
	def shutdown(self):
		if self.client.running:
			self.log('[crescendo] Stopping client...',flush=True)
		
		try:
			self.server.stop()
		except:
			pass
		
		self.client.stop()
		
		if len(self.node_list):
			self.log('[crescendo] Killing node connections',flush=True)
			self.disconnect_node_list()
		else: self.log('[crescendo] No node connections to kill',flush=True)
		
		self.running = False
	
	def tick(self,using_thread=False):
		try:	
			while self.running:
				if self.can_search: threading.Timer(5,self.populate_node_list,()).start();self.can_search = False
				self.connect_node_list()
				if len(self._log): print self._log.pop(0)
		except KeyboardInterrupt:
			self.running = False
		
		if not using_thread: self.shutdown()

if __name__ == "__main__":
	_c = crescendo()
	_c.populate_node_list()
	
	if len(sys.argv)==2 and sys.argv[1]=='-server':
		_c.start_server()
	
	_c.tick()
