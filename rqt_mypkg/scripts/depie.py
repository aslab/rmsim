#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depie.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from talker2 import talker

class Ui_Form(object):
	def message(self):
		print ('Robominer en pie')
		talker()
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(600, 210)
		self.gridLayout = QtWidgets.QGridLayout(Form)
		self.gridLayout.setObjectName("gridLayout")
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setObjectName("pushButton")
		self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

		self.retranslateUi(Form)
		self.pushButton.clicked.connect(self.message)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Widget para levantar el robot"))
		self.pushButton.setText(_translate("Form", "De pie!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

