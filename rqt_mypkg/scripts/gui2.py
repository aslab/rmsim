#!/usr/bin/env python

import sys
from gui2_ui import *
import rospy
from pos_listener import *
from depie_talker import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pos_talker import *

rospy.init_node('robominer_pos_GUI', anonymous=True)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    msg = pyqtSignal(str, str, int)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setupThreads()
        self.num = pos_listener()
        self.num.msg.connect(self.updateLCD)
        self.num.start()
        #self.msg.connect(self.printslot)
        self.lineEdit.setValidator(QIntValidator())
        self.lineEdit.setMaxLength(4)
        #self.lineEdit.returnPressed.connect(self.send_pos)
        #self.pushButton_en_pie.clicked.connect(self.en_pie_slot)
        self.comboBox_art.activated[str].connect(self.show_lim)

    def updateLCD(self, value0, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20, value21, value22, value23):
        self.lcdNumber_rev3_r1.display(value9)
        self.lcdNumber_rev3_r2.display(value10)
        self.lcdNumber_rev3_r3.display(value11)
        self.lcdNumber_rev3_l1.display(value6)
        self.lcdNumber_rev3_l2.display(value7)
        self.lcdNumber_rev3_l3.display(value8)
        self.lcdNumber_rev5_r1.display(value15)
        self.lcdNumber_rev5_r2.display(value16)
        self.lcdNumber_rev5_r3.display(value17)
        self.lcdNumber_rev5_l1.display(value12)
        self.lcdNumber_rev5_l2.display(value13)
        self.lcdNumber_rev5_l3.display(value14)
        self.lcdNumber_rev8_r1.display(value21)
        self.lcdNumber_rev8_r2.display(value22)
        self.lcdNumber_rev8_r3.display(value23)
        self.lcdNumber_rev8_l1.display(value18)
        self.lcdNumber_rev8_l2.display(value19)
        self.lcdNumber_rev8_l3.display(value20)
        self.lcdNumber_rev11_r1.display(value3)
        self.lcdNumber_rev11_r2.display(value4)
        self.lcdNumber_rev11_r3.display(value5)
        self.lcdNumber_rev11_l1.display(value0)
        self.lcdNumber_rev11_l2.display(value1)
        self.lcdNumber_rev11_l3.display(value2)

    @pyqtSlot()
    def enableButton(self):
        self.pushButton_en_pie.setEnabled(False)

    @pyqtSlot()
    def done(self):
        self.pushButton_en_pie.setEnabled(True)
        #QTimer.singleShot(5000, lambda: self.pushButton_en_pie.setDisabled(False))

    def setupThreads(self):
        #Hilo para ponerlo en pie
        self.thread = QThread()
        self.enpie = depie_talker()
        self.enpie.moveToThread(self.thread)
        self.thread.started.connect(self.enpie.run)
        self.pushButton_en_pie.clicked.connect(self.enpie.talker)
        self.enpie.wait_for_input.connect(self.enableButton)
        self.enpie.done.connect(self.done)

        #Hilo para ordenes individuales
        self.thread2 = QThread()
        self.set_pos = set_pos()
        self.set_pos.moveToThread(self.thread2)
        self.thread2.started.connect(self.set_pos.run)
        self.lineEdit.returnPressed.connect(self.send_pos)

        #Conectamos
        self.msg.connect(self.set_pos.talker2)

        # Start threads
        self.thread.start()
        self.thread2.start()

    def send_pos(self):
        self.msg.emit(self.comboBox_pata.currentText(), self.comboBox_art.currentText(), int(self.lineEdit.text()))
        self.lineEdit.clear()

    def talker2(self, pata, art, ang):
        print(pata)
        print(art)
        print(ang)

    def show_lim(self, text):
        #Limites: Rev3: -110 110 Rev5: -110 110 Rev8: -45 180 Rev11: -90 90
        if text[0] == 'E':
            self.label_limits.setText('Rango:')
        if text == 'Rev3':
            self.label_limits.setText('Rango: [-110,110]')
        if text == 'Rev5':
            self.label_limits.setText('Rango: [-110,110]')
        if text == 'Rev8':
            self.label_limits.setText('Rango: [-45,180]')
        if text == 'Rev11':
            self.label_limits.setText('Rango: [-90,90]')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())