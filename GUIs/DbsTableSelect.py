# -*- coding: utf-8 -*-

from views.UI_DbsTableSelect import Ui_DbsTableSelect
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from libs import dbsConnector
from GUIs.Threads.RfTableListsThread import RfTableListsThread
from libs import GL


class DbsTableSelect(QWidget, Ui_DbsTableSelect):
    backSignal = pyqtSignal()

    def __init__(self, conf, parent=None):
        super(DbsTableSelect, self).__init__(parent)
        self.setupUi(self)
        self.conf = conf
        self.mydb = dbsConnector(self.conf)
        self.tables_raw = None
        self.getTableNames()

    def getTableNames(self):
        self.tableNamesWidget.clear()
        self.getTableThread = RfTableListsThread(self.conf)
        self.getTableThread.trigger.connect(self.finish_getTableNames)
        self.getTableThread.start()

    def finish_getTableNames(self):
        self.tables_raw = GL.tables_lists
        for table in self.tables_raw:
            self.tableNamesWidget.addItem(table[0])

    def backClicked(self):
        self.backSignal.emit()

    def tableSelected(self, clicked_item):
        self.chooseButton.setEnabled(True)
        # 右侧浏览窗口数据刷新
        print(clicked_item.text())

    def refreshClicked(self):
        self.chooseButton.setEnabled(False)
        self.tableNamesWidget.clear()
        self.tableNamesWidget.setEnabled(False)
        refresh_item = QListWidgetItem()
        refresh_item.setFlags(QtCore.Qt.NoItemFlags)
        refresh_item.setText("正在刷新...")
        self.tableNamesWidget.addItem(refresh_item)
        # 多线程，获取table names
        self.getTableNames()
        self.tableNamesWidget.setEnabled(True)

    def chooseClicked(self):
        print(self.tableNamesWidget.currentItem().text())
