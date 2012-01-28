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
		
		self.info = {'nodes':0}
		
		self.crescendo = Crescendo_Thread(self)
		self.crescendo.start()
	
	def add_client(self,name):
		
		self.ui.lst_clients.addItem(name)
	
	def add_node(self,name):
		self.info['nodes']+=1
		
		self.ui.lst_nodes.addItem(name)
		self.ui.lab_connected_nodes.setText('Connected nodes: %s' % str(self.info['nodes']))
		
		#self.change_node('10.234.16.131','shut')
	
	def change_node(self,name,newname):
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == name:
				self.ui.lst_nodes.item(row).setText(newname)
	
	def closeEvent(self, event):
		self.crescendo.shutdown()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	servergui = Crescendo_GUI()
	servergui.show()
	sys.exit(app.exec_())