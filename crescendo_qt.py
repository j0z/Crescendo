import os, sys, json, threading, sys
from PyQt4 import QtCore, QtGui

if '-metro' in sys.argv:
	from ui_josh import Ui_MainWindow
else:
	from ui import Ui_MainWindow

from ui_profile import Ui_Dialog

import crescendo

class Crescendo_Thread(QtCore.QThread):
	def __init__(self,gui):
		self.client = crescendo.crescendo(callback=gui)
		
		QtCore.QThread.__init__(self)
	
	def set_download_progress(self,progress,file):
		self.emit(QtCore.SIGNAL("output(int,QString)"), int(progress),file)
	
	def got_file_list(self):
		self.emit(QtCore.SIGNAL("None"))
	
	def shutdown(self):
		self.client.shutdown()
	
	def run(self):
		if not '-noserver' in sys.argv:
			self.client.start_server()
		
		self.client.populate_node_list()
		self.client.tick(using_thread=True)

class profile_GUI(QtGui.QDialog):
	def __init__(self,parent):
		QtGui.QWidget.__init__(self, parent)
		
		self.parent = parent
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		
		self.ui.cmb_profiles.currentIndexChanged.connect(self.select_profile)
		self.profile = None
		self.profiles = None
		
		self.ui.btn_connect.clicked.connect(self.connect_profile)
	
	def accept(self):
		self.save_profile()
		self.close()
	
	def closeEvent(self, event): 
		pass
	
	def connect_profile(self):
		self.parent.crescendo.client.connect_profile(self.profile)
	
	def select_profile(self):
		if not self.profiles: return
		
		for _profile in self.profiles:
			_current = str(self.ui.cmb_profiles.itemText(self.ui.cmb_profiles.currentIndex()))
			
			if _current in [_profile['name'],_profile['host']]:
				self.load_profile(_profile)
				break
		
		if _current=='New Profile':
			self.new_profile()
			self.load_profile(self.profile,clear=True)
	
	def new_profile(self):
		self.profile = {}
	
	def save_profile(self):
		self.profile['name'] = str(self.ui.lne_name.text())
		self.profile['host'] = str(self.ui.lne_ip.text())
		self.profile['port'] = int(self.ui.lne_port.text())
		self.profile['username'] = str(self.ui.lne_username.text())
		self.profile['password'] = str(self.ui.lne_password.text())
		self.profile['security'] = str(self.ui.cmb_security.currentText())
		self.profile['auto_connect'] = self.ui.chk_auto_connect.isChecked()
		
		self.parent.crescendo.client.add_profile(self.profile)
		
		print 'Profile updated'
	
	def load_profile(self,profile,clear=False):
		self.profile = profile
		
		if clear:
			self.ui.lne_name.clear()
			self.ui.lne_ip.clear()
			self.ui.lne_port.clear()
			self.ui.lne_username.clear()
			self.ui.lne_password.clear()
			self.ui.chk_auto_connect.setChecked(False)
			self.ui.cmb_security.setCurrentIndex(0)
			return
		
		self.ui.lne_name.setText(profile['name'])
		self.ui.lne_ip.setText(profile['host'])
		self.ui.lne_port.setText(str(profile['port']))
		
		_find = self.ui.cmb_profiles.findText(profile['name'],QtCore.Qt.MatchFlags(QtCore.Qt.MatchExactly))
		self.ui.cmb_profiles.setCurrentIndex(_find)
		
		if profile.has_key('security'):
			_find = self.ui.cmb_security.findText(profile['security'],QtCore.Qt.MatchFlags(QtCore.Qt.MatchExactly))
		else:
			_find = None
		
		if not _find==None:
			self.ui.cmb_security.setCurrentIndex(_find)
		
		if profile.has_key('username'):
			self.ui.lne_username.setText(profile['username'])
		else:
			self.ui.lne_username.clear()
		
		if profile.has_key('password'):
			self.ui.lne_password.setText(profile['password'])
		else:
			self.ui.lne_password.clear()
		
		if profile.has_key('auto_connect'):
			self.ui.chk_auto_connect.setChecked(profile['auto_connect'])
	
	def load_profile_list(self,profiles):
		self.ui.cmb_profiles.clear()
		self.ui.cmb_profiles.addItem('New Profile')
		
		self.profiles = profiles
		
		for entry in profiles:
			if entry.has_key('name') and entry['name']=='Unknown':
				self.ui.cmb_profiles.addItem(entry['host'])
			else:
				self.ui.cmb_profiles.addItem(entry['name'])

class Crescendo_GUI(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QtGui.QIcon(os.path.join('gfx','icon.ico')))
		
		self.info = {'nodes':[]}
		
		self.profilegui = profile_GUI(self)
		
		self.crescendo = Crescendo_Thread(self)
		self.crescendo.start()
		
		self.connect(self.crescendo, QtCore.SIGNAL("output(int,QString)"), self.set_download_progress)
		self.connect(self.crescendo, QtCore.SIGNAL("None"), self.select_node)
		self.ui.cmb_newslist.currentIndexChanged.connect(self.select_newslist)
		self.ui.lst_nodes.itemClicked.connect(self.select_node)
		self.ui.lst_nodes.itemDoubleClicked.connect(self.show_dialog)
		self.ui.btn_grab.clicked.connect(self.grab_file)
		self.ui.btn_connect.clicked.connect(self.show_dialog_new)
		self.ui.btn_clear_downloads.clicked.connect(self.clear_downloads)
		self.ui.lne_filter.textChanged.connect(self.filter)
	
	def log(self,text):
		self.ui.lst_log.insertItem(0,text)
	
	def show_dialog(self):
		_current = str(self.ui.lst_nodes.currentItem().text())
		_profile = self.crescendo.client.has_profile(host=_current,name=_current)
		
		self.profilegui.load_profile_list(self.crescendo.client.profiles)
		self.profilegui.load_profile(_profile)
		self.profilegui.show()
	
	def show_dialog_new(self):
		#_profile = self.crescendo.client.new_profile()
		
		self.profilegui.load_profile_list(self.crescendo.client.profiles)
		self.profilegui.new_profile()
		self.profilegui.show()
	
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
		#Check to see if the host/name/whatever is already on the list
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == name:
				return
		
		self.ui.lst_nodes.addItem(name)
		self.info['nodes'].append({'name':name,'files':[]})
		
		#Can't believe I'm doing this.
		#TODO: Since we're just adding onto the list, we can just get the
		#length of the list and set the color of the latest one...
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == name:
				self.ui.lst_nodes.item(row).setTextColor(QtGui.QColor(128,128,128))
	
	def update_node(self,node,info):
		self.ui.lab_connected_nodes.setText('Connected nodes: %s' % str(len(self.info['nodes'])))
		
		for row in range(self.ui.lst_nodes.count()):
			if self.ui.lst_nodes.item(row).text() == node:
				self.ui.lst_nodes.item(row).setText(info['name'])
				
				_find = self.ui.cmb_newslist.findText(node,QtCore.Qt.MatchFlags(QtCore.Qt.MatchExactly))
				
				if info.has_key('news') and _find==-1:
					self.info['nodes'][row]['news'] = info['news']
					self.ui.cmb_newslist.addItem(info['name'])
				
				self.info['nodes'][row]['host'] = self.info['nodes'][row]['name']
				self.info['nodes'][row]['name'] = info['name']
				self.info['nodes'][row]['files'] = info['files']
				self.ui.lst_nodes.item(row).setTextColor(QtGui.QColor(0,0,0))
				
				break
	
	def select_node(self,filter=None):
		self.ui.lst_files.clear()
		
		for selected in self.ui.lst_nodes.selectedItems():
			_n = self.ui.lst_nodes.row(selected)
			
			if _n>=len(self.info['nodes']): _n=len(self.info['nodes'])-1
			
			for file in self.info['nodes'][_n]['files']:
				_filesize = int(file['size'])
				_temp_filesize = int(file['size'])

				if _temp_filesize > 1000000: _filesize ='%s MB' % (_temp_filesize/1000000)
				else: _filesize ='%s kb' % (_temp_filesize/1024)
				
				if isinstance(filter,str):
					if not file['name'].lower().count(filter.lower()): continue
				
				i=QtGui.QTreeWidgetItem([file['name'],str(_filesize),file['root'],selected.text()])
				self.ui.lst_files.addTopLevelItem(i)
	
	def select_newslist(self,selected=None):
		_selected = str(self.ui.cmb_newslist.itemText(selected))
		
		for node in self.info['nodes']:
			if node['name']==_selected and node.has_key('news'):
				self.ui.txt_news.setHtml(node['news'])
				break
		
	def connect_node(self):
		if self.ui.lne_ip.text().count(':'):	
			_h,_p = self.ui.lne_ip.text().split(':')
			self.crescendo.client.add_node((_h,int(_p)))
			self.ui.lne_ip.setText('')
			
	def grab_file(self):
		_nr = -1
		
		for selected in self.ui.lst_files.selectedItems():
			#if self.ui.lst_files.currentItem():
			for _n in range(self.ui.lst_nodes.count()):
				if self.ui.lst_nodes.item(_n).text()==selected.text(3):
					_nr = _n
					break
			
			#if _nr==-1:
			#	print 'Pick a file first.'
			#	return
			
			_name= selected.text(0)
			_size = selected.text(1)
			_path = selected.text(2)
			
			_type = str(selected.text(1).split(' ')[1])
			_temp_filesize = int(selected.text(1).split(' ')[0])
			if _type == 'kb': _filesize = _temp_filesize*1024
			elif _type == 'MB': _filesize = _temp_filesize*1000000
			
			i=QtGui.QTreeWidgetItem([_name,str(0),_size,_path])
			self.ui.lst_queue.addTopLevelItem(i)
			
			_h = self.info['nodes'][_nr]['host']
			
			self.crescendo.client.get_file(_h,_name)
	
	def filter(self):
		self.select_node(filter=str(self.ui.lne_filter.text()))
	
	def clear_downloads(self):
		_search = self.ui.lst_queue.findItems('100.00',QtCore.Qt.MatchFlags(QtCore.Qt.MatchContains),column=1)
		
		for _i in _search:
			self.ui.lst_queue.takeTopLevelItem(self.ui.lst_queue.indexFromItem(_i).row())
	
	def grabbed_file(self,file):
		self.ui.lab_downloaded_files.setText('Downloaded files: %s' % str(len(self.crescendo.client.downloaded_files)))
	
	def set_download_progress(self,progress,file):
		file = json.loads(str(file))
		
		_temp_filesize = int(progress)
		
		self.ui.prg_download.setMaximum(file['size'])
		
		if _temp_filesize>=self.ui.prg_download.value():
			self.ui.prg_download.setValue(_temp_filesize)
		
		if _temp_filesize > 1000000: _filesize ='%s MB' % (_temp_filesize/1000000)
		else: _filesize ='%s kb' % (_temp_filesize/1024)
		
		if _temp_filesize>=file['size']:
			self.ui.prg_download.setValue(0)
		
		_percent = (progress/float(self.ui.prg_download.maximum()))*100.0
		if _percent>100: _percent = 100
		
		#TODO: Send over file path and double check it.
		_search = self.ui.lst_queue.findItems(file['name'],QtCore.Qt.MatchFlags(QtCore.Qt.MatchRecursive))[0]
		_search.setText(1,_filesize+' (%.2f%%)' % _percent)
	
	def closeEvent(self, event):
		self.crescendo.shutdown()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	servergui = Crescendo_GUI()
	servergui.show()
	sys.exit(app.exec_())
