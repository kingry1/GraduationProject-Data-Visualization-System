# -*- coding: utf-8 -*-

from views.UI_DbsTableSelect import Ui_DbsTableSelect
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QDesktopWidget, QFileDialog
from PyQt5.QtCore import pyqtSignal
from GUIs.Threads.RfTableListsThread import RfTableListsThread
from GUIs.Threads.ShowTablesThread import ShowTablesThread
from libs.PandasModel import PandasModel
from libs import GL
from libs.DdbsConnector import DbsConnector


class DbsTableSelect(QWidget, Ui_DbsTableSelect):
    backSignal = pyqtSignal()
    visualizationSignal = pyqtSignal(dict, str)

    def __init__(self, conf, parent=None):
        super(DbsTableSelect, self).__init__(parent)
        self.setupUi(self)
        self.center()
        self.conf = conf
        self.tables_raw = None
        self.getTableNames()

    def center(self):  # 主窗口居中显示函数
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def getTableNames(self):
        self.tableNamesWidget.clear()
        self.getTableThread = RfTableListsThread(self.conf)
        self.getTableThread.trigger.connect(self.finish_getTableNames)
        self.getTableThread.start()

    def finish_getTableNames(self):
        self.tables_raw = GL.tables_lists
        for table in self.tables_raw:
            self.tableNamesWidget.addItem(table)

    def backClicked(self):
        self.backSignal.emit()

    def tableSelected(self, clicked_item):
        self.chooseButton.setEnabled(True)
        # 右侧浏览窗口数据刷新
        self.showTableThread = ShowTablesThread(self.conf, clicked_item.text())
        self.showTableThread.trigger.connect(self.showTableContent)
        self.showTableThread.start()

    def showTableContent(self):
        self.tableModel = PandasModel(GL.tables_df)
        self.tableView.setModel(self.tableModel)
        self.tableView.scrollToTop()

    def refreshClicked(self):
        self.chooseButton.setEnabled(False)
        self.tableNamesWidget.clear()
        self.tableNamesWidget.setEnabled(False)
        refresh_item = QListWidgetItem()
        refresh_item.setFlags(QtCore.Qt.NoItemFlags)
        refresh_item.setText("Refreshing...")
        self.tableNamesWidget.addItem(refresh_item)
        # 多线程，获取table names
        self.getTableNames()
        self.tableNamesWidget.setEnabled(True)

    def chooseClicked(self):
        self.visualizationSignal.emit(self.conf, self.tableNamesWidget.currentItem().text())

    def addExcel(self):
        file_path, file_type = QFileDialog.getOpenFileName(self,
                                                           "Choose Excel File",
                                                           "/",  # 起始路径
                                                           "Excel Files (*.xls *.xlsx)")
        if file_path == "":
            return

        DbsConnector.add_excel(file_path=file_path, conf=self.conf)

    def addJSON(self):
        file_path, file_type = QFileDialog.getOpenFileName(self,
                                                           "Choose JSON File",
                                                           "/",  # 起始路径
                                                           "JSON Files (*.json)")
        if file_path == "":
            return

        DbsConnector.add_json(file_path=file_path, conf=self.conf)

    def addCSV(self):
        file_path, file_type = QFileDialog.getOpenFileName(self,
                                                           "Choose CSV File",
                                                           "/",  # 起始路径
                                                           "CSV Files (*.csv)")
        if file_path == "":
            return

        DbsConnector.add_json(file_path=file_path, conf=self.conf)
