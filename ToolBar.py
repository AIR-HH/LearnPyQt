#!/usr/bin/python
# -*- coding : utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        exitAct = QAction(QIcon('1.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        toolbar = QToolBar()
        toolbar.addAction(exitAct)
        self.addToolBar(toolbar)
        #self.toolbar = self.addToolBar("Exit")
        #self.toolbar.addAction(exitAct)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setGeometry(300, 300, 300, 270)
        self.setWindowTitle('Toolbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())