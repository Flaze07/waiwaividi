# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 301, 31))
        self.label.setStyleSheet("#label {\n"
"    font-size: 20pt\n"
"}")
        self.label.setObjectName("label")
        self.linkLineEdit = QtWidgets.QLineEdit(Form)
        self.linkLineEdit.setGeometry(QtCore.QRect(20, 50, 591, 51))
        self.linkLineEdit.setStyleSheet("#linkLineEdit {\n"
"    font-size: 17pt\n"
"}")
        self.linkLineEdit.setObjectName("linkLineEdit")
        self.dlOptionComboBox = QtWidgets.QComboBox(Form)
        self.dlOptionComboBox.setGeometry(QtCore.QRect(620, 50, 161, 51))
        self.dlOptionComboBox.setStyleSheet("#dlOptionComboBox {\n"
"    font-size: 15pt;\n"
"}")
        self.dlOptionComboBox.setObjectName("dlOptionComboBox")
        self.dlOptionComboBox.addItem("")
        self.dlButton = QtWidgets.QPushButton(Form)
        self.dlButton.setGeometry(QtCore.QRect(275, 120, 250, 60))
        self.dlButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dlButton.setStyleSheet("#dlButton {\n"
"    font-size: 15pt;\n"
"}")
        self.dlButton.setObjectName("dlButton")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(110, 230, 671, 61))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressLabel = QtWidgets.QLabel(Form)
        self.progressLabel.setGeometry(QtCore.QRect(20, 190, 301, 31))
        self.progressLabel.setStyleSheet("#progressLabel {\n"
"    font-size: 13pt\n"
"}")
        self.progressLabel.setObjectName("progressLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WaiwaiVidi"))
        self.label.setText(_translate("Form", "Insert Youtube Link Here"))
        self.linkLineEdit.setText(_translate("Form", "https://youtube.com"))
        self.dlOptionComboBox.setItemText(0, _translate("Form", "1080p60fps"))
        self.dlButton.setText(_translate("Form", "Download"))
        self.progressLabel.setText(_translate("Form", "Progress"))
