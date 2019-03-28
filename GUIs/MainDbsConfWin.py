# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QInputDialog
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, pyqtSignal
from views.UI_MainDbsConfWin import Ui_MainDbsConfWin
from libs.DdbsConnector import DbsConnector
from libs import GL
import os


class MainDbsConfWin(QMainWindow, Ui_MainDbsConfWin):
    callDbsTableSignal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(MainDbsConfWin, self).__init__(parent)
        self.setupUi(self)
        self.dbsDic = GL.dbsDic
        self.clickedDatabaseName = None
        self.clickedDatabaseItem = None
        for dbsName in sorted(self.dbsDic.keys()):
            item = QListWidgetItem()
            item.setText(dbsName)
            self.listWidget.addItem(item)
        self.typeComboBox.addItem('请选择数据库类型')

        # add validator
        hostRegexp = QRegExp(
            "^((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))$")
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
        self.databaseNameLine.setText(self.dbsDic[self.clickedDatabaseName]['name'])
        self.typeComboBox.clear()
        self.typeComboBox.addItems(GL.dbsTypes)
        index = self.typeComboBox.findText(self.dbsDic[self.clickedDatabaseName]['type'])
        self.typeComboBox.setCurrentIndex(index)

        self.set_button_status(True)

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
        # check connection
        try:
            DbsConnector.test_connection(self.dbsDic[self.clickedDatabaseName])
        except Exception as err:
            self.statusbar.showMessage(str(err))
            return

        # 这里将选中的数据库传给下一个页面
        self.callDbsTableSignal.emit(self.dbsDic[self.clickedDatabaseName])

    def addClicked(self):
        dbsName, ok = QInputDialog.getText(self, '新建数据库', '输入数据库名称                  ')
        if ok:
            self.listWidget.addItem(dbsName)
            GL.new_dbs(dbsName=dbsName)

    def editClicked(self):
        # set lineEdit enable
        self.set_input_status(True)

    def deleteClicked(self):
        self.listWidget.takeItem(self.listWidget.row(self.clickedDatabaseItem))
        GL.dbsDic.pop(self.clickedDatabaseName)
        self.set_input_status(False)
        self.hostLine.setText('')
        self.portLine.setText('')
        self.userLine.setText('')
        self.passwordLine.setText('')
        self.databaseNameLine.setText('')
        self.typeComboBox.clear()
        self.typeComboBox.addItem('请选择数据库类型')
        self.set_button_status(False)
        GL.save_dbs()

    def saveDatabaseConf(self):
        self.set_input_status(False)
        host = self.hostLine.text()
        port = self.portLine.text()
        user = self.userLine.text()
        password = self.passwordLine.text()
        name = self.databaseNameLine.text()
        _type = self.typeComboBox.currentText()

        GL.dbsDic[self.clickedDatabaseName]['host'] = host
        GL.dbsDic[self.clickedDatabaseName]['port'] = port
        GL.dbsDic[self.clickedDatabaseName]['user'] = user
        GL.dbsDic[self.clickedDatabaseName]['password'] = password
        GL.dbsDic[self.clickedDatabaseName]['name'] = name
        GL.dbsDic[self.clickedDatabaseName]['type'] = _type
        GL.save_dbs()

    def set_input_status(self, bool):
        self.hostLine.setEnabled(bool)
        self.portLine.setEnabled(bool)
        self.userLine.setEnabled(bool)
        self.passwordLine.setEnabled(bool)
        self.databaseNameLine.setEnabled(bool)
        self.typeComboBox.setEnabled(bool)

    def set_button_status(self, bool):
        self.connectButton.setEnabled(bool)
        self.deleteButton.setEnabled(bool)
        self.editButton.setEnabled(bool)
