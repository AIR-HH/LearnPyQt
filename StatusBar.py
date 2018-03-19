#!/usr/bin/python3
# -*- coding : utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage("This is StatusBar")
        self.setGeometry(400,400,400,400)
        self.setWindowTitle("StatusBar")
        self.show()
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

