import sys, threading
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow

import crescendo

class Crescendo_Thread(QtCore.QThread):
	def __init__(self,gui):
		self.client = crescendo.crescendo(callback=gui)
		
		QtCore.QThread.__init__(self)
	
	def shutdown(self):
		self.client.shutdown()
	
	def run(self):
		#self.client.start_server()
		self.client.populate_node_list()
		self.client.tick(using_thread=True)

class Crescendo_GUI(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('gfx\\icon.ico'))
		
		self.info = {'nodes':[]}
		
		#QtCore.QObject.connect(self.ui.lst_nodes, QtCore.SIGNAL('currentItemChanged()'), self.select_node)
		self.ui.lst_nodes.currentItemChanged.connect(self.select_node)
		
		self.crescendo = Crescendo_Thread(self)
		self.crescendo.start()
	
	def add_node(self,name):
		self.info['nodes'].append({'name':name,'files':[]})
		
		self.ui.lst_nodes.addItem(name)
		self.ui.lab_connected_nodes.setText('Connected nodes: %s' % str(len(self.info['nodes'])))
	
	def update_node(self,node,info):
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == node:
				self.ui.lst_nodes.item(row).setText(info['name'])
				self.info['nodes'][row]['name'] = info['name']
				self.info['nodes'][row]['files'] = info['files']
				
				break
	
	def select_node(self):
		print 'wut'
		self.ui.lst_files.clear()
		
		_n = self.ui.lst_nodes.currentRow()
		
		for file in self.info['nodes'][_n]['files']:
			item=QtGui.QTreeWidgetItem([file['name'],str(file['size']/1024)])
			self.ui.lst_files.addTopLevelItem(item)
			#self.ui.lst_files.addItem(str(file['name']))
	
	def closeEvent(self, event):
		self.crescendo.shutdown()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	servergui = Crescendo_GUI()
	servergui.show()
	sys.exit(app.exec_())