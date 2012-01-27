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
		self.client.populate_node_list()
		self.client.tick()

class Crescendo_GUI(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('gfx\\icon.ico'))
		
		self.crescendo = Crescendo_Thread(self)
		self.crescendo.start()
	
	def add_client(self,name):
		self.ui.lst_clients.addItem(name)
	
	def add_node(self,name):
		self.ui.lst_nodes.addItem(name)
	
	def closeEvent(self, event):
		self.crescendo.shutdown()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	servergui = Crescendo_GUI()
	servergui.show()
	sys.exit(app.exec_())