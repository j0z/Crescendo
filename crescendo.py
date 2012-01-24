#/usr/bin/python
import subprocess
import crescendo_server as server
import crescendo_search as search

class crescendo:
	def __init__(self):
		self.client_list = []

	def log(self,text):
		print text
	
	def start_server(self):
		#server.
		pass

	def populate_client_list(self):
		self.log('[search.Engine] Running search.Engine')
		try:
			_s = search.Engine()
			_s.start()
			self.log('[search.Engine] Search invoked and starting')
		except:
			self.log('[search.Engine] Failed.')
			return False
		
		while _s.is_running(): pass
		
		if _s.has_clients():
			self.client_list = _s.get_clients()
			self.log('[search.Engine] Found: %s' % len(self.client_list))
		else:
			self.log('[search.Engine] No clients found')

_c = crescendo()
_c.populate_client_list()
