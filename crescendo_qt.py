import sys, threading, sys
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
	
	def shutdown(self):
		self.client.shutdown()
	
	def run(self):
		if '-server' in sys.argv:
			self.client.start_server()
		
		self.client.populate_node_list()
		#threading.Timer(10,self.client.populate_node_list,()).start()
		self.client.tick(using_thread=True)

class Crescendo_GUI(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('gfx\\icon.ico'))
		
		self.info = {'nodes':[]}
		
		self.ui.lst_nodes.currentItemChanged.connect(self.select_node)
		self.ui.btn_grab.clicked.connect(self.grab_file)
		self.ui.btn_connect.clicked.connect(self.connect_node)
		
		self.crescendo = Crescendo_Thread(self)
		self.crescendo.start()
	
	def log(self,text):
		self.ui.lst_log.insertItem(0,text)
	
	def remove_node(self,node):
		for row in range(self.ui.lst_nodes.count()):
			print str(self.ui.lst_nodes.item(row).text()),node
			if str(self.ui.lst_nodes.item(row).text()) == node:
				self.ui.lst_nodes.takeItem(row)
	
	def add_node(self,name):
		self.info['nodes'].append({'name':name,'files':[]})
		
		self.ui.lst_nodes.addItem(name)
		self.ui.lab_connected_nodes.setText('Connected nodes: %s' % str(len(self.info['nodes'])))
	
	def update_node(self,node,info):
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == node:
				self.ui.lst_nodes.item(row).setText(info['name'])
				self.info['nodes'][row]['host'] = self.info['nodes'][row]['name']
				self.info['nodes'][row]['name'] = info['name']
				self.info['nodes'][row]['files'] = info['files']
				
				break
	
	def select_node(self):
		self.ui.lst_files.clear()
		
		_n = self.ui.lst_nodes.currentRow()
		
		for file in self.info['nodes'][_n]['files']:
			item=QtGui.QTreeWidgetItem([file['name'],str(file['size']/1024)])
			self.ui.lst_files.addTopLevelItem(item)
	
	def connect_node(self):
		if self.ui.lne_ip.text().count(':'):	
			_h,_p = self.ui.lne_ip.text().split(':')
			self.crescendo.client.add_node((_h,int(_p)))
			self.ui.lne_ip.setText('')
	
	def grab_file(self):
		_nr = self.ui.lst_nodes.currentRow()
		_fr = self.ui.lst_files.currentItem().text(0)
		
		_h = self.info['nodes'][_nr]['host']
		_f = _fr#_h['files'][_fr]
		
		self.crescendo.client.get_file(_h,_f)
	
	def closeEvent(self, event):
		self.crescendo.shutdown()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	servergui = Crescendo_GUI()
	servergui.show()
	sys.exit(app.exec_())
