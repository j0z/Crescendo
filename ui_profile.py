# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\profile.ui'
#
# Created: Sat Feb 11 13:39:40 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(240, 250)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cmb_profiles = QtGui.QComboBox(Dialog)
        self.cmb_profiles.setObjectName(_fromUtf8("cmb_profiles"))
        self.cmb_profiles.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.cmb_profiles)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.lne_ip = QtGui.QLineEdit(Dialog)
        self.lne_ip.setMaxLength(15)
        self.lne_ip.setObjectName(_fromUtf8("lne_ip"))
        self.gridLayout_3.addWidget(self.lne_ip, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.lne_name = QtGui.QLineEdit(Dialog)
        self.lne_name.setObjectName(_fromUtf8("lne_name"))
        self.gridLayout_3.addWidget(self.lne_name, 0, 1, 1, 1)
        self.lne_port = QtGui.QLineEdit(Dialog)
        self.lne_port.setObjectName(_fromUtf8("lne_port"))
        self.gridLayout_3.addWidget(self.lne_port, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.lne_username = QtGui.QLineEdit(Dialog)
        self.lne_username.setObjectName(_fromUtf8("lne_username"))
        self.gridLayout_2.addWidget(self.lne_username, 2, 2, 1, 1)
        self.cmb_security = QtGui.QComboBox(Dialog)
        self.cmb_security.setObjectName(_fromUtf8("cmb_security"))
        self.cmb_security.addItem(_fromUtf8(""))
        self.cmb_security.addItem(_fromUtf8(""))
        self.cmb_security.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cmb_security, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.lne_password = QtGui.QLineEdit(Dialog)
        self.lne_password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lne_password.setObjectName(_fromUtf8("lne_password"))
        self.gridLayout_2.addWidget(self.lne_password, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.chk_auto_connect = QtGui.QCheckBox(Dialog)
        self.chk_auto_connect.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chk_auto_connect.setObjectName(_fromUtf8("chk_auto_connect"))
        self.verticalLayout_2.addWidget(self.chk_auto_connect)
        self.btn_yesno = QtGui.QDialogButtonBox(Dialog)
        self.btn_yesno.setOrientation(QtCore.Qt.Horizontal)
        self.btn_yesno.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btn_yesno.setObjectName(_fromUtf8("btn_yesno"))
        self.verticalLayout_2.addWidget(self.btn_yesno)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_yesno, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.btn_yesno, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Edit Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_profiles.setItemText(0, QtGui.QApplication.translate("Dialog", "New Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "    Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Security:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_security.setItemText(0, QtGui.QApplication.translate("Dialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_security.setItemText(1, QtGui.QApplication.translate("Dialog", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_security.setItemText(2, QtGui.QApplication.translate("Dialog", "auth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Pass:", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_auto_connect.setText(QtGui.QApplication.translate("Dialog", "Connect on startup", None, QtGui.QApplication.UnicodeUTF8))

