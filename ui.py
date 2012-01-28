# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main.ui'
#
# Created: Sat Jan 28 13:39:29 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(560, 561)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(560, 561))
        MainWindow.setMaximumSize(QtCore.QSize(560, 561))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(560, 520))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 521, 221))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lab_connected_nodes = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lab_connected_nodes.setObjectName(_fromUtf8("lab_connected_nodes"))
        self.verticalLayout_2.addWidget(self.lab_connected_nodes)
        self.lab_downloaded_files = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lab_downloaded_files.setObjectName(_fromUtf8("lab_downloaded_files"))
        self.verticalLayout_2.addWidget(self.lab_downloaded_files)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 521, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lst_nodes = QtGui.QListWidget(self.gridLayoutWidget)
        self.lst_nodes.setObjectName(_fromUtf8("lst_nodes"))
        self.gridLayout.addWidget(self.lst_nodes, 0, 5, 1, 1)
        self.btn_info_node = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_info_node.setObjectName(_fromUtf8("btn_info_node"))
        self.gridLayout.addWidget(self.btn_info_node, 1, 5, 1, 1)
        self.lst_clients = QtGui.QListWidget(self.gridLayoutWidget)
        self.lst_clients.setObjectName(_fromUtf8("lst_clients"))
        self.gridLayout.addWidget(self.lst_clients, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btn_info_client = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_info_client.setObjectName(_fromUtf8("btn_info_client"))
        self.horizontalLayout_5.addWidget(self.btn_info_client)
        self.btn_kick = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_kick.setObjectName(_fromUtf8("btn_kick"))
        self.horizontalLayout_5.addWidget(self.btn_kick)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CrescendoQt", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_connected_nodes.setText(QtGui.QApplication.translate("MainWindow", "Connected nodes: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_downloaded_files.setText(QtGui.QApplication.translate("MainWindow", "Downloaded files:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Clients/Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_info_node.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_info_client.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_kick.setText(QtGui.QApplication.translate("MainWindow", "Kick", None, QtGui.QApplication.UnicodeUTF8))

