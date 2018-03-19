#!python
# -*- coding : utf-8 -*-
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon
import sys
class Example(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self) :
        lbl1 = QLabel('zetcode',self)
        lbl1.move(15,10)
        
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)
        
        self.setWindowIcon(QIcon('1.jpg'))
        self.statusBar()
        self.setGeometry(400,400,400,400)
        self.setWindowTitle("Absolute")
        self.show()
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex  = Example()
    sys.exit(app.exec_())