import random
from PyQt5.QtCore import QThread, pyqtSignal
import time


class pos_receiver(QThread):

    msg = pyqtSignal(int)

    def run(self):
        for x in range(10):
            time.sleep(1)
            self.msg.emit(random.randint(1, 101))

th1 = Thread(target=listener)
th1.start()

for x in range(10):
    rospy.sleep(1)
    print(callback.pos[1])