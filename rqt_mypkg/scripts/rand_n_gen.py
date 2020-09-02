import random
from PyQt5.QtCore import QThread, pyqtSignal
import time


class rand_n_gen(QThread):

    msg = pyqtSignal(int)

    def run(self):
        for x in range(10):
            time.sleep(1)
#            self.msg.emit(random.randint(1, 101))
            self.msg.emit(2000)
