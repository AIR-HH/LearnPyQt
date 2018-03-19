#!/user/bin/python
# -*- coding : utf-8 -*- 

import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #QAction是菜单栏、工具栏或者快捷键的动作的组合
        #设置图标文字
        exitAct = QAction(QIcon('342.png'),'&Exit',self)
        #设置快捷键
        exitAct.setShortcut('Ctrl+Q')
        #设置状态栏显示
        exitAct.setStatusTip('Exit application')
        #设置消息
        exitAct.triggered.connect(qApp.quit)
        
        self.statusBar().showMessage("This menu statusbar")

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setWindowIcon(QIcon("1.jpg"))
        self.setWindowTitle("Menu")
        self.setGeometry(500,500,500,500)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())