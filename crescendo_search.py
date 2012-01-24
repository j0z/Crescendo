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
			_out += '...found!'
			self.engine.working.append(self)
		except:
			_out += '...failed'
		
		print _out

		self.engine.active.remove(self)
		#self.hostname = socket.gethostname()

class Engine(threading.Thread):
	def __init__(self):
		self.ip_list = ['10.232.16.242','10.0.50.98']
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
			if not len(self.active) and len(self.working):
				#if len(self.working)==1: print '1 working host.'
				#elif len(self.working)>1: print '%s working hosts.', len(self.working)

				self.running = False
		
	def has_clients(self):
		if len(self.working): return True
	
	def get_clients(self):
		return self.working
