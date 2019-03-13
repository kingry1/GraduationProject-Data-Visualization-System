# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QInputDialog
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, pyqtSignal
from views.UI_MainDbsConfWin import Ui_MainDbsConfWin
from libs import GL


class MainDbsConfWin(QMainWindow, Ui_MainDbsConfWin):
    callDbsTableSignal = pyqtSignal(dict)

    def __init__(self, parent=None):
        print("new main")
        super(MainDbsConfWin, self).__init__(parent)
        self.setupUi(self)
        self.dbsDic = GL.dbsDic
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
            GL.dbsDic[newName] = GL.dbsDic.pop(oldName)
            GL.save_dbs()

    def connectClicked(self):
        # 这里将选中的数据库传给下一个页面
        self.callDbsTableSignal.emit(self.dbsDic[self.clickedDatabaseName])

    def addClicked(self):
        dbsName, ok = QInputDialog.getText(self, '新建数据库', '输入数据库名称                  ')
        if ok:
            self.listWidget.addItem(dbsName)
            GL.new_dbs(dbsName=dbsName)

    def editClicked(self):
        # set lineEdit enable
        self.hostLine.setEnabled(True)
        self.portLine.setEnabled(True)
        self.userLine.setEnabled(True)
        self.passwordLine.setEnabled(True)

    def deleteClicked(self):
        self.listWidget.takeItem(self.listWidget.row(self.clickedDatabaseItem))
        GL.dbsDic.pop(self.clickedDatabaseName)
        self.hostLine.setEnabled(False)
        self.portLine.setEnabled(False)
        self.userLine.setEnabled(False)
        self.passwordLine.setEnabled(False)
        self.hostLine.setText('')
        self.portLine.setText('')
        self.userLine.setText('')
        self.passwordLine.setText('')
        self.connectButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.editButton.setEnabled(False)
        GL.save_dbs()

    def saveDatabaseConf(self):
        self.hostLine.setEnabled(False)
        self.portLine.setEnabled(False)
        self.userLine.setEnabled(False)
        self.passwordLine.setEnabled(False)
        host = self.hostLine.text()
        port = self.portLine.text()
        user = self.userLine.text()
        password = self.passwordLine.text()
        GL.dbsDic[self.clickedDatabaseName]['host'] = host
        GL.dbsDic[self.clickedDatabaseName]['port'] = port
        GL.dbsDic[self.clickedDatabaseName]['user'] = user
        GL.dbsDic[self.clickedDatabaseName]['password'] = password
        GL.save_dbs()
