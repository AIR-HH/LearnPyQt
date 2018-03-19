#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QToolTip,QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore  import QSize,QCoreApplication

class Example(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()
        self.center()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btu = QPushButton("",self)
        btu.setToolTip("This is a <b>QpushButton</b> widget")
        btu.resize(51,51)
        btu.move(50,50)
        btu.setIcon(QIcon("342.png"))
        btu.setIconSize(QSize(51,51))
        btu.setStyleSheet("QPushButton{border-radius : 50% ;}")
        btu.clicked.connect(QCoreApplication.instance().quit)
        self.setGeometry(300,300,200,220)
        self.setWindowTitle('ICON')
        self.setWindowIcon(QIcon("1.jpg"))
        self.show()
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    w = Example()
    sys.exit(app.exec_())
'''
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(300, 300)
    w.setWindowTitle('AIR')
    w.show()
    
    sys.exit(app.exec_())
'''