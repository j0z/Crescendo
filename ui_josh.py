# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_josh.ui'
#
# Created: Mon Feb 13 15:23:51 2012
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
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
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
        self.line.setGeometry(QtCore.QRect(119, 38, 16, 339))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
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
        self.lst_files.setGeometry(QtCore.QRect(129, 38, 647, 316))
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
"    color:rgb(26,26,26);\n"
"    border: 0px solid rgb(176,176,176);\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background:rgb(220,220,220);\n"
"    border:rgb(220,220,220);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QHeaderView {\n"
"    background: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: white;\n"
"    border: 0px solid white;\n"
"    padding-left: 0px;\n"
"\n"
"    }\n"
"\n"
"\n"
"QHeaderView::down-arrow {\n"
"     image: url(down-arrow.png);\n"
" }\n"
" QHeaderView::up-arrow {\n"
"     image: url(up-arrow.png);\n"
" }\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"))
        self.lst_files.setFrameShape(QtGui.QFrame.NoFrame)
        self.lst_files.setFrameShadow(QtGui.QFrame.Plain)
        self.lst_files.setLineWidth(0)
        self.lst_files.setIndentation(0)
        self.lst_files.setRootIsDecorated(False)
        self.lst_files.setHeaderHidden(False)
        self.lst_files.setObjectName(_fromUtf8("lst_files"))
        self.lst_files.headerItem().setBackground(1, QtGui.QColor(120, 0, 0))
        self.lst_files.header().setVisible(True)
        self.lst_files.header().setDefaultSectionSize(200)
        self.lst_files.header().setSortIndicatorShown(True)
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
        self.lst_nodes.setGeometry(QtCore.QRect(0, 38, 116, 339))
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
"    color:rgb(26,26,26);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background:rgb(220,220,220);\n"
"    border:rgb(220,220,220);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 10px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"))
        self.lst_nodes.setFrameShape(QtGui.QFrame.NoFrame)
        self.lst_nodes.setFrameShadow(QtGui.QFrame.Plain)
        self.lst_nodes.setLineWidth(0)
        self.lst_nodes.setObjectName(_fromUtf8("lst_nodes"))
        self.btn_grab = QtGui.QPushButton(self.centralwidget)
        self.btn_grab.setGeometry(QtCore.QRect(657, 355, 117, 22))
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
"    color: rgb(26,26,26);\n"
"    background-color:rgb(176,176,176);\n"
"\n"
"}"))
        self.btn_grab.setDefault(True)
        self.btn_grab.setFlat(True)
        self.btn_grab.setObjectName(_fromUtf8("btn_grab"))
        self.btn_connect = QtGui.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(693, 2, 105, 26))
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
        self.btn_connect.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btn_connect.setFont(font)
        self.btn_connect.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"    color: rgb(26,26,26);\n"
"    background-color:rgb(176,176,176);\n"
"\n"
"}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../gfx/gear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_connect.setIcon(icon)
        self.btn_connect.setIconSize(QtCore.QSize(16, 16))
        self.btn_connect.setDefault(True)
        self.btn_connect.setFlat(True)
        self.btn_connect.setObjectName(_fromUtf8("btn_connect"))
        self.lne_filter = QtGui.QLineEdit(self.centralwidget)
        self.lne_filter.setGeometry(QtCore.QRect(129, 359, 256, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lne_filter.setFont(font)
        self.lne_filter.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    border: 2px solid rgb(121,121,121);\n"
"    selection-background-color: rgb(176,176,176);\n"
"    selection-color: rgb(26,26,26);\n"
"}"))
        self.lne_filter.setObjectName(_fromUtf8("lne_filter"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(2, 383, 801, 199))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8("QTabBar {\n"
"    border: 0px solid white;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"     background: white;\n"
"     border: 0px solid white;\n"
"     border-bottom-color: white; /* same as the pane color */\n"
"     border-top-left-radius: 0px;\n"
"     border-top-right-radius: 0px;\n"
"     min-width: 8ex;\n"
"     padding: 5px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     background: white;\n"
"     color: rgb(26,26,26);\n"
" }\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: black;\n"
"}\n"
"\n"
" QTabBar::tab:!selected {\n"
"    margin-top: 5px; /* make non-selected tabs look smaller */\n"
"    color: rgb(76,76,76);\n"
" }"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lab_downloaded_files = QtGui.QLabel(self.tab)
        self.lab_downloaded_files.setGeometry(QtCore.QRect(522, 25, 251, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.lab_downloaded_files.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.lab_downloaded_files.setFont(font)
        self.lab_downloaded_files.setObjectName(_fromUtf8("lab_downloaded_files"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(7, -20, 38, 21))
        palette = QtGui.QPalette()
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lab_connected_nodes = QtGui.QLabel(self.tab)
        self.lab_connected_nodes.setGeometry(QtCore.QRect(521, 2, 252, 21))
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
        self.lab_connected_nodes.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.lab_connected_nodes.setFont(font)
        self.lab_connected_nodes.setObjectName(_fromUtf8("lab_connected_nodes"))
        self.lst_log = QtGui.QListWidget(self.tab)
        self.lst_log.setGeometry(QtCore.QRect(0, 0, 515, 124))
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
"    color:rgb(26,26,26);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background:rgb(220,220,220);\n"
"    border:rgb(220,220,220);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 10px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"))
        self.lst_log.setFrameShape(QtGui.QFrame.NoFrame)
        self.lst_log.setFrameShadow(QtGui.QFrame.Plain)
        self.lst_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lst_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lst_log.setObjectName(_fromUtf8("lst_log"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.txt_news = QtGui.QTextBrowser(self.tab_4)
        self.txt_news.setGeometry(QtCore.QRect(-2, -1, 798, 131))
        self.txt_news.setStyleSheet(_fromUtf8("QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 10px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"))
        self.txt_news.setObjectName(_fromUtf8("txt_news"))
        self.cmb_newslist = QtGui.QComboBox(self.tab_4)
        self.cmb_newslist.setGeometry(QtCore.QRect(639, 132, 155, 20))
        self.cmb_newslist.setStyleSheet(_fromUtf8(" QComboBox {\n"
"     border: 1px solid rgb(121,121,121);\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 6em;\n"
" }\n"
"\n"
" QComboBox:editable {\n"
"     background: white;\n"
" }\n"
"\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"      background: white;\n"
" }\n"
"\n"
" /* QComboBox gets the \"on\" state when the popup is open */\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"     background: white;\n"
" }\n"
"\n"
" QComboBox:on { /* shift the text when the popup opens */\n"
"     padding-top: 3px;\n"
"     padding-left: 4px;\n"
" }\n"
"\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
" QComboBox::down-arrow {\n"
"     image: url(/ui/down-arrow.png);\n"
" }\n"
"\n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"     top: 1px;\n"
"     left: 1px;\n"
" }\n"
"\n"
" QComboBox QAbstractItemView {\n"
"     border: 1px solid rgb(26,26,26);\n"
"     selection-background-color: rgb(176,176,176);\n"
"    color:rgb(26,26,26)\n"
" }"))
        self.cmb_newslist.setFrame(False)
        self.cmb_newslist.setObjectName(_fromUtf8("cmb_newslist"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lst_queue = QtGui.QTreeWidget(self.tab_2)
        self.lst_queue.setGeometry(QtCore.QRect(-1, -1, 797, 122))
        self.lst_queue.setStyleSheet(_fromUtf8("QTreeWidget {\n"
"    show-decoration-selected: 1;\n"
"    border: 4px solid white;\n"
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
"    color:rgb(26,26,26);\n"
"    border: 0px solid rgb(176,176,176);\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background:rgb(220,220,220);\n"
"    border:rgb(220,220,220);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QHeaderView {\n"
"    background: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: white;\n"
"    border: 0px solid white;\n"
"    padding-left: 0px;\n"
"\n"
"    }\n"
"QHeaderView::down-arrow {\n"
"     image: url(down-arrow.png);\n"
" }\n"
" QHeaderView::up-arrow {\n"
"     image: url(up-arrow.png);\n"
" }\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(0,0,0,0);\n"
"    width: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(121,121,121);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(26,26,26);\n"
"    min-height: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: white;\n"
"    height: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}"))
        self.lst_queue.setAnimated(True)
        self.lst_queue.setObjectName(_fromUtf8("lst_queue"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lst_queue.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lst_queue.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lst_queue.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lst_queue.headerItem().setFont(3, font)
        self.lst_queue.header().setDefaultSectionSize(100)
        self.lst_queue.header().setMinimumSectionSize(100)
        self.btn_clear_downloads = QtGui.QPushButton(self.tab_2)
        self.btn_clear_downloads.setGeometry(QtCore.QRect(0, 123, 121, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.btn_clear_downloads.setFont(font)
        self.btn_clear_downloads.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"    color: rgb(26,26,26);\n"
"    background-color:rgb(176,176,176);\n"
"}"))
        self.btn_clear_downloads.setDefault(True)
        self.btn_clear_downloads.setFlat(True)
        self.btn_clear_downloads.setObjectName(_fromUtf8("btn_clear_downloads"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.prg_download = QtGui.QProgressBar(self.centralwidget)
        self.prg_download.setGeometry(QtCore.QRect(3, 590, 797, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prg_download.setFont(font)
        self.prg_download.setStyleSheet(_fromUtf8(" QProgressBar {\n"
"     border: 0px solid white;\n"
"     border-radius: 0px;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: rgb(176,176,176);\n"
"     width: 5px;\n"
" }\n"
"\n"
" QProgressBar {\n"
"     border: 0px solid white;\n"
"     border-radius: 0px;\n"
"     text-align: center;\n"
" }"))
        self.prg_download.setProperty("value", 0)
        self.prg_download.setInvertedAppearance(False)
        self.prg_download.setFormat(_fromUtf8(""))
        self.prg_download.setObjectName(_fromUtf8("prg_download"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CrescendoQt", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "NODES", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_files.setSortingEnabled(True)
        self.lst_files.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "| FILE", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_files.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "| SIZE", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_files.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "| PATH", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_files.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "| NODE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "FILES", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_grab.setText(QtGui.QApplication.translate("MainWindow", "DOWNLOAD", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_connect.setText(QtGui.QApplication.translate("MainWindow", "PROFILES", None, QtGui.QApplication.UnicodeUTF8))
        self.lne_filter.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "FILTER", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_downloaded_files.setText(QtGui.QApplication.translate("MainWindow", "Downloaded Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_connected_nodes.setText(QtGui.QApplication.translate("MainWindow", "Connected Nodes: ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "INFO", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "NEWS", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_queue.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "| FILE", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_queue.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "| PROGRESS", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_queue.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "| SIZE", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_queue.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "| PATH", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear_downloads.setText(QtGui.QApplication.translate("MainWindow", "CLEAR DOWNLOADS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "QUEUE", None, QtGui.QApplication.UnicodeUTF8))

