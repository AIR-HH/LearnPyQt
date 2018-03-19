#!/user/bin/python
# -*- coding : utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QMenu,qApp


class Example(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.initUI()
    def initUI(self):

        self.setWindowTitle("Right Menu")
        self.setGeometry(500,500,500,500)
        self.show()
    #重载弹出式菜单事件
    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())