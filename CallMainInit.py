# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.MainInit import Ui_MainWindow
import global_var


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.dbsDic = global_var.dbsDic
        for dbsName in self.dbsDic.keys():
            self.listWidget.addItem(dbsName)

    def select(self):
        print("aaaa")

    def edit(self):
        print("aaaa")

    def delete(self):
        print("aaaa")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
