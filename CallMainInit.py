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
        self.clickedDatabase = ''
        for dbsName in self.dbsDic.keys():
            self.listWidget.addItem(dbsName)

    def listClicked(self, clicked_item):
        self.clickedDatabase = clicked_item.text()
        self.hostLine.setText(self.dbsDic[self.clickedDatabase]['host'])
        self.portLine.setText(self.dbsDic[self.clickedDatabase]['port'])
        self.userLine.setText(self.dbsDic[self.clickedDatabase]['user'])
        self.passwordLine.setText(self.dbsDic[self.clickedDatabase]['password'])

    def selectClicked(self):
        # 这里将选中的数据库传给下一个页面
        print("传给下一个页面的数据:", self.dbsDic)

    def editClicked(self):
        # set lineEdit enable
        self.hostLine.setEnabled(True)
        self.portLine.setEnabled(True)
        self.userLine.setEnabled(True)
        self.passwordLine.setEnabled(True)
        print(self.dbsDic)

    def deleteClicked(self):
        print(self.dbsDic)

    def saveDatabaseConf(self):
        self.hostLine.setEnabled(False)
        self.portLine.setEnabled(False)
        self.userLine.setEnabled(False)
        self.passwordLine.setEnabled(False)
        host = self.hostLine.text()
        port = self.portLine.text()
        user = self.userLine.text()
        password = self.passwordLine.text()
        global_var.dbsDic[self.clickedDatabase]['host'] = host
        global_var.dbsDic[self.clickedDatabase]['port'] = port
        global_var.dbsDic[self.clickedDatabase]['user'] = user
        global_var.dbsDic[self.clickedDatabase]['password'] = password
        global_var.save_dbs()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())