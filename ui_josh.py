# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\ir8llama\crescendo\Crescendo\ui\main.ui'
#
# Created: Sun Jan 29 21:13:54 2012
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
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(560, 561))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(119, 38, 3, 294))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(4, 348, 804, 310))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.groupBox_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(22)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(_fromUtf8(""))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(3, 36, 796, 199))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lab_downloaded_files = QtGui.QLabel(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        self.lab_downloaded_files.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_downloaded_files.setFont(font)
        self.lab_downloaded_files.setObjectName(_fromUtf8("lab_downloaded_files"))
        self.verticalLayout_2.addWidget(self.lab_downloaded_files)
        self.lab_connected_nodes = QtGui.QLabel(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lab_connected_nodes.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_connected_nodes.setFont(font)
        self.lab_connected_nodes.setObjectName(_fromUtf8("lab_connected_nodes"))
        self.verticalLayout_2.addWidget(self.lab_connected_nodes)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.lst_log = QtGui.QListWidget(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_log.sizePolicy().hasHeightForWidth())
        self.lst_log.setSizePolicy(sizePolicy)
        self.lst_log.setMaximumSize(QtCore.QSize(800, 600))
        self.lst_log.setStyleSheet(_fromUtf8("QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background:rgb(200,200,200);\n"
"}\n"
"\n"
"QListView:item:selected:!active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background:rgb(176,176,176);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background:rgb(220,220,220);\n"
"    border:rgb(220,200,200);\n"
"}"))
        self.lst_log.setFrameShape(QtGui.QFrame.NoFrame)
        self.lst_log.setFrameShadow(QtGui.QFrame.Plain)
        self.lst_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lst_log.setObjectName(_fromUtf8("lst_log"))
        self.verticalLayout_2.addWidget(self.lst_log)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -3, 101, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("Qlabel{\n"
"    color:rgb(26, 26, 26);\n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.lst_files = QtGui.QTreeWidget(self.centralwidget)
        self.lst_files.setGeometry(QtCore.QRect(129, 38, 647, 294))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_files.sizePolicy().hasHeightForWidth())
        self.lst_files.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.lst_files.setPalette(palette)
        self.lst_files.setStyleSheet(_fromUtf8("QTreeWidget {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background:rgb(200,200,200);\n"
"}\n"
"\n"
"QTreeWidget:item:selected:!active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QTreeWidget::item:selected:active {\n"
"    background:rgb(176,176,176);\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background:rgb(220,220,220);\n"
"    border:rgb(220,200,200);\n"
"}\n"
"\n"
"QTreeWidget::header {\n"
"    background: white;\n"
"}"))
        self.lst_files.setFrameShape(QtGui.QFrame.NoFrame)
        self.lst_files.setFrameShadow(QtGui.QFrame.Plain)
        self.lst_files.setLineWidth(0)
        self.lst_files.setIndentation(0)
        self.lst_files.setRootIsDecorated(False)
        self.lst_files.setObjectName(_fromUtf8("lst_files"))
        self.lst_files.headerItem().setBackground(1, QtGui.QColor(120, 0, 0))
        self.lst_files.header().setVisible(False)
        self.lst_files.header().setDefaultSectionSize(200)
        self.lst_files.header().setSortIndicatorShown(False)
        self.lst_files.header().setStretchLastSection(False)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, -2, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lst_nodes = QtGui.QListWidget(self.centralwidget)
        self.lst_nodes.setGeometry(QtCore.QRect(0, 38, 116, 294))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_nodes.sizePolicy().hasHeightForWidth())
        self.lst_nodes.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.lst_nodes.setPalette(palette)
        self.lst_nodes.setStyleSheet(_fromUtf8("QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background:rgb(200,200,200);\n"
"}\n"
"\n"
"QListView:item:selected:!active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background:rgb(176,176,176);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background:rgb(220,220,220);\n"
"    border:rgb(220,220,220);\n"
"}"))
        self.lst_nodes.setFrameShape(QtGui.QFrame.NoFrame)
        self.lst_nodes.setFrameShadow(QtGui.QFrame.Plain)
        self.lst_nodes.setLineWidth(0)
        self.lst_nodes.setObjectName(_fromUtf8("lst_nodes"))
        self.btn_grab = QtGui.QPushButton(self.centralwidget)
        self.btn_grab.setGeometry(QtCore.QRect(659, 338, 117, 29))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.btn_grab.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btn_grab.setFont(font)
        self.btn_grab.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"    color: black;\n"
"    background-color:rgb(176,176,176);\n"
"\n"
"}"))
        self.btn_grab.setDefault(True)
        self.btn_grab.setFlat(True)
        self.btn_grab.setObjectName(_fromUtf8("btn_grab"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CrescendoQt", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "INFORMATION", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_downloaded_files.setText(QtGui.QApplication.translate("MainWindow", "Downloaded files:", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_connected_nodes.setText(QtGui.QApplication.translate("MainWindow", "Connected nodes: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "NODES", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_files.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "FILE", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_files.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "SIZE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "FILES", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_grab.setText(QtGui.QApplication.translate("MainWindow", "DOWNLOAD", None, QtGui.QApplication.UnicodeUTF8))
