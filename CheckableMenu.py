#!/usr/bin/python
# -*- coding : utf-8 -*- 
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&FILE")
        act = QAction("View",self,checkable = True)
        act.setStatusTip("This is checkable menu")
        act.setChecked(True)
        act.triggered.connect(self.tooggleMenu)

        fileMenu.addAction(act)
        self.statusbar = self.statusBar()
        self.setWindowTitle("CheckableMenu")
        self.setGeometry(500,500,500,500)
        self.show()
    def tooggleMenu(self,state):
        if state :
            self.statusbar.show()
        else : 
            self.statusbar.hide()
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())