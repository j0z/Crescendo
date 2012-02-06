import os, sys, threading, sys
from PyQt4 import QtCore, QtGui

if '-metro' in sys.argv:
	from ui_josh import Ui_MainWindow
else:
	from ui import Ui_MainWindow

import crescendo

class Crescendo_Thread(QtCore.QThread):
	def __init__(self,gui):
		self.client = crescendo.crescendo(callback=gui)
		
		QtCore.QThread.__init__(self)
	
	def set_download_progress(self,progress):
		self.emit(QtCore.SIGNAL("output(int)"), int(progress))
	
	def shutdown(self):
		self.client.shutdown()
	
	def run(self):
		if '-server' in sys.argv:
			self.client.start_server()
		
		self.client.populate_node_list()
		self.client.tick(using_thread=True)

class files:
	def __init__(self):
		self.files = []
		self.parents = []
		self.roots = []
	
	def has_parent(self,name):
		for parent in self.parents:
			if parent == name: return True
		
		return False
	
	def make_parent(self,name):
		if not self.has_parent(name):
			print 'Added parent: '+name
			self.parents.append(name)
			
	def has_root(self,name):
		for root in self.roots:
			if root == name: return True
		
		return False
	
	def make_root(self,name):
		if not self.has_root(name):
			print 'Added root: '+name
			self.roots.append(name)
	
	def has_file(self,name):
		for file in self.files:
			if file == name: return True
		
		return False
	
	def make_file(self,name):
		if not self.has_file(name):
			print 'Added file: '+name
			self.files.append(name)

class Crescendo_GUI(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('gfx\\icon.ico'))
		
		self.info = {'nodes':[]}
		
		self.files = files()
			
		self.crescendo = Crescendo_Thread(self)
		self.crescendo.start()
		
		self.connect(self.crescendo, QtCore.SIGNAL("output(int)"), self.set_download_progress)
		self.ui.lst_nodes.currentItemChanged.connect(self.select_node)
		self.ui.btn_grab.clicked.connect(self.grab_file)
		self.ui.btn_connect.clicked.connect(self.connect_node)
		self.ui.prg_download.setValue(0)
	
	def log(self,text):
		self.ui.lst_log.insertItem(0,text)
	
	def remove_node(self,node):
		_rlist = []
		
		for row in range(self.ui.lst_nodes.count()):
			if str(self.ui.lst_nodes.item(row).text()) == node:
				self.info['nodes'].pop(row)
				_rlist.append(row)
		
		#PYTHON HAS FEATURES OTHER PROGRAMMING LANGUAGES DON'T HAVE XD
		[self.ui.lst_nodes.takeItem(row) for row in _rlist]
		
		self.ui.lab_connected_nodes.setText('Connected nodes: %s' % str(len(self.info['nodes'])))
	
	def add_node(self,name):
		self.info['nodes'].append({'name':name,'files':[]})
		
		self.ui.lst_nodes.addItem(name)
		
		#Can't believe I'm doing this.
		#TODO: Since we're just adding onto the list, we can just get the
		#length of the list and set the color of the latest one...
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == name:
				self.ui.lst_nodes.item(row).setTextColor(QtGui.QColor(128,128,128))
		
		#TODO: Should this be in update_node?
		#Maybe a node is dead, but still on the list for whatever reason.
		self.ui.lab_connected_nodes.setText('Connected nodes: %s' % str(len(self.info['nodes'])))
	
	def update_node(self,node,info):
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == node:
				self.ui.lst_nodes.item(row).setText(info['name'])
				self.info['nodes'][row]['host'] = self.info['nodes'][row]['name']
				self.info['nodes'][row]['name'] = info['name']
				self.info['nodes'][row]['files'] = info['files']
				self.ui.lst_nodes.item(row).setTextColor(QtGui.QColor(0,0,0))
				
				break
	
	def select_node(self):
		self.ui.lst_files.clear()
		
		_n = self.ui.lst_nodes.currentRow()
		
		#Clear list
		#takeTopLevelItem
		
		if _n>=len(self.info['nodes']): _n=len(self.info['nodes'])-1
		
		self.rlist = []
		
		for file in self.info['nodes'][_n]['files']:
			for parent in file['parents']:
				if len(parent):
					self.files.make_parent(parent)
				else:
					root_item=QtGui.QTreeWidgetItem(['root',str(0)])
					self.ui.lst_files.addTopLevelItem(root_item)
			
			#for root in file['root']:
			#if len(parent):
			self.files.make_root(file['root'])
			
			for _f in file['files']:
				self.files.make_file(_f)
		
		for parent in self.files.parents:
			t=QtGui.QTreeWidgetItem([parent,str(0)])
			root_item.addChild(t)
			root_item=t
		
		for file in self.files.files:
		
			#hahahah this is the worst code I've ever written
			_sf = file.split('/')
			if len(_sf) == 1:
				_sf = file.split('\\')
			#print _sf[len(_sf)-1]
			
			f = self.ui.lst_files.findItems(QtCore.QString(_sf[len(_sf)-2]),QtCore.Qt.MatchFlags(QtCore.Qt.MatchRecursive))
			try:
				print repr(f[0])
				QtGui.QTreeWidgetItem(f[0],[_sf[len(_sf)-1],str(0)])
			except:
				print 'Let\'s be honest: I\'ve been doing this all week. This failing is the only issue I have right now, so everyone can deal with it.'

	
	def connect_node(self):
		if self.ui.lne_ip.text().count(':'):	
			_h,_p = self.ui.lne_ip.text().split(':')
			self.crescendo.client.add_node((_h,int(_p)))
			self.ui.lne_ip.setText('')
			
	def grab_file(self):
		_nr = self.ui.lst_nodes.currentRow()
		_fr = self.ui.lst_files.currentItem().text(0)
		
		_type = str(self.ui.lst_files.currentItem().text(1).split(' ')[1])
		_temp_filesize = int(self.ui.lst_files.currentItem().text(1).split(' ')[0])
		if _type == 'kb': _filesize = _temp_filesize*1024
		elif _type == 'MB': _filesize = _temp_filesize*1000000
		
		self.ui.prg_download.setMaximum(_filesize)
		
		_h = self.info['nodes'][_nr]['host']
		_f = _fr
		
		self.crescendo.client.get_file(_h,_f)
	
	def grabbed_file(self,file):
		self.ui.lab_downloaded_files.setText('Downloaded files: %s' % str(len(self.crescendo.client.downloaded_files)))
	
	def set_download_progress(self,progress):
		self.ui.prg_download.setValue(self.ui.prg_download.value()+int(progress))
	
	def closeEvent(self, event):
		self.crescendo.shutdown()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	servergui = Crescendo_GUI()
	servergui.show()
	sys.exit(app.exec_())
