# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pos_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 459)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_rev3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rev3.sizePolicy().hasHeightForWidth())
        self.label_rev3.setSizePolicy(sizePolicy)
        self.label_rev3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rev3.setObjectName("label_rev3")
        self.gridLayout.addWidget(self.label_rev3, 4, 0, 1, 1)
        self.label_r1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_r1.sizePolicy().hasHeightForWidth())
        self.label_r1.setSizePolicy(sizePolicy)
        self.label_r1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_r1.setObjectName("label_r1")
        self.gridLayout.addWidget(self.label_r1, 3, 1, 1, 1)
        self.label_r2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_r2.sizePolicy().hasHeightForWidth())
        self.label_r2.setSizePolicy(sizePolicy)
        self.label_r2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_r2.setObjectName("label_r2")
        self.gridLayout.addWidget(self.label_r2, 3, 2, 1, 1)
        self.label_r3 = QtWidgets.QLabel(self.centralwidget)
        self.label_r3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_r3.setObjectName("label_r3")
        self.gridLayout.addWidget(self.label_r3, 3, 3, 1, 1)
        self.label_l1 = QtWidgets.QLabel(self.centralwidget)
        self.label_l1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_l1.setObjectName("label_l1")
        self.gridLayout.addWidget(self.label_l1, 3, 4, 1, 1)
        self.label_l2 = QtWidgets.QLabel(self.centralwidget)
        self.label_l2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_l2.setObjectName("label_l2")
        self.gridLayout.addWidget(self.label_l2, 3, 5, 1, 1)
        self.label_l3 = QtWidgets.QLabel(self.centralwidget)
        self.label_l3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_l3.setObjectName("label_l3")
        self.gridLayout.addWidget(self.label_l3, 3, 6, 1, 1)
        self.lcdNumber_rev3_r1 = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_rev3_r1.sizePolicy().hasHeightForWidth())
        self.lcdNumber_rev3_r1.setSizePolicy(sizePolicy)
        self.lcdNumber_rev3_r1.setObjectName("lcdNumber_rev3_r1")
        self.gridLayout.addWidget(self.lcdNumber_rev3_r1, 4, 1, 1, 1)
        self.lcdNumber_rev3_r2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev3_r2.setObjectName("lcdNumber_rev3_r2")
        self.gridLayout.addWidget(self.lcdNumber_rev3_r2, 4, 2, 1, 1)
        self.lcdNumber_rev3_r3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev3_r3.setObjectName("lcdNumber_rev3_r3")
        self.gridLayout.addWidget(self.lcdNumber_rev3_r3, 4, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 6, 1, 1)
        self.label_giro = QtWidgets.QLabel(self.centralwidget)
        self.label_giro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_giro.setObjectName("label_giro")
        self.gridLayout.addWidget(self.label_giro, 1, 5, 1, 1)
        self.lcdNumber_rev3_l1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev3_l1.setObjectName("lcdNumber_rev3_l1")
        self.gridLayout.addWidget(self.lcdNumber_rev3_l1, 4, 4, 1, 1)
        self.lcdNumber_rev3_l2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev3_l2.setObjectName("lcdNumber_rev3_l2")
        self.gridLayout.addWidget(self.lcdNumber_rev3_l2, 4, 5, 1, 1)
        self.lcdNumber_rev3_l3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev3_l3.setObjectName("lcdNumber_rev3_l3")
        self.gridLayout.addWidget(self.lcdNumber_rev3_l3, 4, 6, 1, 1)
        self.lcdNumber_rev5_r1 = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_rev5_r1.sizePolicy().hasHeightForWidth())
        self.lcdNumber_rev5_r1.setSizePolicy(sizePolicy)
        self.lcdNumber_rev5_r1.setObjectName("lcdNumber_rev5_r1")
        self.gridLayout.addWidget(self.lcdNumber_rev5_r1, 5, 1, 1, 1)
        self.lcdNumber_rev5_r2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev5_r2.setObjectName("lcdNumber_rev5_r2")
        self.gridLayout.addWidget(self.lcdNumber_rev5_r2, 5, 2, 1, 1)
        self.lcdNumber_rev5_r3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev5_r3.setObjectName("lcdNumber_rev5_r3")
        self.gridLayout.addWidget(self.lcdNumber_rev5_r3, 5, 3, 1, 1)
        self.lcdNumber_rev5_l1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev5_l1.setObjectName("lcdNumber_rev5_l1")
        self.gridLayout.addWidget(self.lcdNumber_rev5_l1, 5, 4, 1, 1)
        self.lcdNumber_rev5_l2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev5_l2.setObjectName("lcdNumber_rev5_l2")
        self.gridLayout.addWidget(self.lcdNumber_rev5_l2, 5, 5, 1, 1)
        self.lcdNumber_rev5_l3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev5_l3.setObjectName("lcdNumber_rev5_l3")
        self.gridLayout.addWidget(self.lcdNumber_rev5_l3, 5, 6, 1, 1)
        self.lcdNumber_rev8_r1 = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_rev8_r1.sizePolicy().hasHeightForWidth())
        self.lcdNumber_rev8_r1.setSizePolicy(sizePolicy)
        self.lcdNumber_rev8_r1.setObjectName("lcdNumber_rev8_r1")
        self.gridLayout.addWidget(self.lcdNumber_rev8_r1, 6, 1, 1, 1)
        self.lcdNumber_rev8_r2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev8_r2.setObjectName("lcdNumber_rev8_r2")
        self.gridLayout.addWidget(self.lcdNumber_rev8_r2, 6, 2, 1, 1)
        self.lcdNumber_rev8_r3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev8_r3.setObjectName("lcdNumber_rev8_r3")
        self.gridLayout.addWidget(self.lcdNumber_rev8_r3, 6, 3, 1, 1)
        self.lcdNumber_rev8_l1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev8_l1.setObjectName("lcdNumber_rev8_l1")
        self.gridLayout.addWidget(self.lcdNumber_rev8_l1, 6, 4, 1, 1)
        self.lcdNumber_rev8_l2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev8_l2.setObjectName("lcdNumber_rev8_l2")
        self.gridLayout.addWidget(self.lcdNumber_rev8_l2, 6, 5, 1, 1)
        self.lcdNumber_rev8_l3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev8_l3.setObjectName("lcdNumber_rev8_l3")
        self.gridLayout.addWidget(self.lcdNumber_rev8_l3, 6, 6, 1, 1)
        self.lcdNumber_rev11_r1 = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_rev11_r1.sizePolicy().hasHeightForWidth())
        self.lcdNumber_rev11_r1.setSizePolicy(sizePolicy)
        self.lcdNumber_rev11_r1.setObjectName("lcdNumber_rev11_r1")
        self.gridLayout.addWidget(self.lcdNumber_rev11_r1, 7, 1, 1, 1)
        self.lcdNumber_rev11_r2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev11_r2.setObjectName("lcdNumber_rev11_r2")
        self.gridLayout.addWidget(self.lcdNumber_rev11_r2, 7, 2, 1, 1)
        self.lcdNumber_rev11_r3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev11_r3.setObjectName("lcdNumber_rev11_r3")
        self.gridLayout.addWidget(self.lcdNumber_rev11_r3, 7, 3, 1, 1)
        self.lcdNumber_rev11_l1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev11_l1.setObjectName("lcdNumber_rev11_l1")
        self.gridLayout.addWidget(self.lcdNumber_rev11_l1, 7, 4, 1, 1)
        self.lcdNumber_rev11_l2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev11_l2.setObjectName("lcdNumber_rev11_l2")
        self.gridLayout.addWidget(self.lcdNumber_rev11_l2, 7, 5, 1, 1)
        self.lcdNumber_rev11_l3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_rev11_l3.setObjectName("lcdNumber_rev11_l3")
        self.gridLayout.addWidget(self.lcdNumber_rev11_l3, 7, 6, 1, 1)
        self.comboBox_art = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_art.sizePolicy().hasHeightForWidth())
        self.comboBox_art.setSizePolicy(sizePolicy)
        self.comboBox_art.setObjectName("comboBox_art")
        self.comboBox_art.addItem("")
        self.comboBox_art.addItem("")
        self.comboBox_art.addItem("")
        self.comboBox_art.addItem("")
        self.comboBox_art.addItem("")
        self.gridLayout.addWidget(self.comboBox_art, 0, 6, 1, 1)
        self.pushButton_en_pie = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_en_pie.sizePolicy().hasHeightForWidth())
        self.pushButton_en_pie.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_en_pie.setFont(font)
        self.pushButton_en_pie.setObjectName("pushButton_en_pie")
        self.gridLayout.addWidget(self.pushButton_en_pie, 0, 1, 2, 2)
        self.label_rev5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rev5.sizePolicy().hasHeightForWidth())
        self.label_rev5.setSizePolicy(sizePolicy)
        self.label_rev5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rev5.setObjectName("label_rev5")
        self.gridLayout.addWidget(self.label_rev5, 5, 0, 1, 1)
        self.label_rev8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rev8.sizePolicy().hasHeightForWidth())
        self.label_rev8.setSizePolicy(sizePolicy)
        self.label_rev8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rev8.setObjectName("label_rev8")
        self.gridLayout.addWidget(self.label_rev8, 6, 0, 1, 1)
        self.label_rev11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rev11.sizePolicy().hasHeightForWidth())
        self.label_rev11.setSizePolicy(sizePolicy)
        self.label_rev11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rev11.setObjectName("label_rev11")
        self.gridLayout.addWidget(self.label_rev11, 7, 0, 1, 1)
        self.comboBox_pata = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pata.setObjectName("comboBox_pata")
        self.comboBox_pata.addItem("")
        self.comboBox_pata.addItem("")
        self.comboBox_pata.addItem("")
        self.comboBox_pata.addItem("")
        self.comboBox_pata.addItem("")
        self.comboBox_pata.addItem("")
        self.comboBox_pata.addItem("")
        self.gridLayout.addWidget(self.comboBox_pata, 0, 5, 1, 1)
        self.label_tit = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tit.sizePolicy().hasHeightForWidth())
        self.label_tit.setSizePolicy(sizePolicy)
        self.label_tit.setMinimumSize(QtCore.QSize(100, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_tit.setFont(font)
        self.label_tit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tit.setObjectName("label_tit")
        self.gridLayout.addWidget(self.label_tit, 2, 2, 1, 4)
        self.label_limits = QtWidgets.QLabel(self.centralwidget)
        self.label_limits.setAlignment(QtCore.Qt.AlignCenter)
        self.label_limits.setObjectName("label_limits")
        self.gridLayout.addWidget(self.label_limits, 2, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Position GUI"))
        self.label_rev3.setText(_translate("MainWindow", "Rev3"))
        self.label_r1.setText(_translate("MainWindow", "Pata r1"))
        self.label_r2.setText(_translate("MainWindow", "Pata r2"))
        self.label_r3.setText(_translate("MainWindow", "Pata r3"))
        self.label_l1.setText(_translate("MainWindow", "Pata l1"))
        self.label_l2.setText(_translate("MainWindow", "Pata l2"))
        self.label_l3.setText(_translate("MainWindow", "Pata l3"))
        self.label_giro.setText(_translate("MainWindow", "Nueva posición (º):"))
        self.comboBox_art.setItemText(0, _translate("MainWindow", "Elija articulación"))
        self.comboBox_art.setItemText(1, _translate("MainWindow", "Rev3"))
        self.comboBox_art.setItemText(2, _translate("MainWindow", "Rev5"))
        self.comboBox_art.setItemText(3, _translate("MainWindow", "Rev8"))
        self.comboBox_art.setItemText(4, _translate("MainWindow", "Rev11"))
        self.pushButton_en_pie.setText(_translate("MainWindow", "Iniciar movimiento"))
        self.label_rev5.setText(_translate("MainWindow", "Rev5"))
        self.label_rev8.setText(_translate("MainWindow", "Rev8"))
        self.label_rev11.setText(_translate("MainWindow", "Rev11"))
        self.comboBox_pata.setItemText(0, _translate("MainWindow", "Elija pata"))
        self.comboBox_pata.setItemText(1, _translate("MainWindow", "Pata r1"))
        self.comboBox_pata.setItemText(2, _translate("MainWindow", "Pata r2"))
        self.comboBox_pata.setItemText(3, _translate("MainWindow", "Pata r3"))
        self.comboBox_pata.setItemText(4, _translate("MainWindow", "Pata l1"))
        self.comboBox_pata.setItemText(5, _translate("MainWindow", "Pata l2"))
        self.comboBox_pata.setItemText(6, _translate("MainWindow", "Pata l3"))
        self.label_tit.setText(_translate("MainWindow", "Ángulo de cada articulación en grados"))
        self.label_limits.setText(_translate("MainWindow", "Rango:"))

