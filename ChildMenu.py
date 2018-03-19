#!/usr/bin/python
# -*- coding : utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMenu,QAction,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        


        act = QAction(QIcon('1.jpg'),"exit",self)
        act.setStatusTip("this is a parents menu")
        act.setShortcut("Ctrl+Q")
        act.triggered.connect(qApp.quit)
        

        iMenu = QMenu('Import',self)
        iMact = QAction(QIcon("1.jpg"),'new',self)
        iMenu.addAction(iMact)
        
        
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addMenu(iMenu)
        fileMenu.addAction(act)
        
        self.statusBar()
        self.setWindowIcon(QIcon("342.png"))
        self.setWindowTitle("Child Menu")
        self.setGeometry(500,500,500,500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())