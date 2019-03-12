# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QInputDialog
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp
from views.MainInit import Ui_MainWindow
import global_var


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.dbsDic = global_var.dbsDic
        self.clickedDatabaseName = ''
        for dbsName in sorted(self.dbsDic.keys()):
            item = QListWidgetItem()
            item.setText(dbsName)
            self.listWidget.addItem(item)

        # add validator
        hostRegexp = QRegExp("^((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))$")
        hostValidator = QRegExpValidator(hostRegexp)
        self.hostLine.setValidator(hostValidator)
        portValidator = QIntValidator(0, 65535)
        self.portLine.setValidator(portValidator)
        userRegexp = QRegExp("^[a-zA-Z0-9_-]{1,}$")
        userValidator = QRegExpValidator(userRegexp)
        self.userLine.setValidator(userValidator)

    def listClicked(self, clicked_item):
        print("clicked", clicked_item.text())
        self.clickedDatabaseItem = clicked_item
        self.clickedDatabaseName = clicked_item.text()
        self.hostLine.setText(self.dbsDic[self.clickedDatabaseName]['host'])
        self.portLine.setText(self.dbsDic[self.clickedDatabaseName]['port'])
        self.userLine.setText(self.dbsDic[self.clickedDatabaseName]['user'])
        self.passwordLine.setText(self.dbsDic[self.clickedDatabaseName]['password'])
        self.connectButton.setEnabled(True)
        self.deleteButton.setEnabled(True)
        self.editButton.setEnabled(True)

    def listDoubleClicked(self, clicked_item):
        oldName = clicked_item.text()
        newName, ok = QInputDialog.getText(self, '修改数据库名称', '输入数据库名称                  ', text=clicked_item.text())
        if ok:
            # check first
            self.clickedDatabaseItem = clicked_item
            self.clickedDatabaseName = newName
            clicked_item.setText(newName)
            global_var.dbsDic[newName] = global_var.dbsDic.pop(oldName)
            global_var.save_dbs()

    def connectClicked(self):
        # 这里将选中的数据库传给下一个页面
        print("传给下一个页面的数据:", self.dbsDic[self.clickedDatabaseName])

    def addClicked(self):
        dbsName, ok = QInputDialog.getText(self, '新建数据库名称', '输入数据库名称                  ')
        if ok:
            self.listWidget.addItem(dbsName)
            global_var.new_dbs(dbsName=dbsName)

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
        global_var.dbsDic[self.clickedDatabaseName]['host'] = host
        global_var.dbsDic[self.clickedDatabaseName]['port'] = port
        global_var.dbsDic[self.clickedDatabaseName]['user'] = user
        global_var.dbsDic[self.clickedDatabaseName]['password'] = password
        global_var.save_dbs()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
