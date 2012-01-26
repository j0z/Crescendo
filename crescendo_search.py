#!/usr/bin/python
import urllib, threading, socket
socket.setdefaulttimeout(5)
 
class HostFinder(threading.Thread):
	def __init__(self, ip, engine, port=9001):
		self.host = (ip,port)
		self.engine = engine

		threading.Thread.__init__(self)

	def get_result(self):
		return self.result
	
	def run(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		try:
			_out = '%s' % self.host[0]
			self.socket.connect(self.host)
			self.engine.add_working(self.host)
			_out += '...found!'
		except:
			_out += '...failed'
		
		self.socket.close()
		
		#print _out

		self.engine.active.remove(self)

class Engine(threading.Thread):
	def __init__(self,parent):
		self.parent = parent

		self.ip_list = ['127.0.0.1','10.234.16.10']
		self.active = []
		self.working = []

		self.running = True

		threading.Thread.__init__(self)

	def is_running(self):
		return self.running

	def run(self):
		while (len(self.ip_list)):
			_f = HostFinder(self.ip_list.pop(),self)
			self.active.append(_f)
			_f.start()

		while (self.running):
			if not len(self.active):
				if len(self.working)==1: self.parent.log('[search.Engine] Found 1 working node')
				elif len(self.working)>1: self.parent.log('[search.Engine] Found %s working nodes' % len(self.working))
				self.running = False
		
	def has_clients(self):
		if len(self.working): return True
	
	def get_clients(self):
		return self.working
	
	def add_working(self,host):
		self.working.append(host)
		self.parent.add_node(host)
