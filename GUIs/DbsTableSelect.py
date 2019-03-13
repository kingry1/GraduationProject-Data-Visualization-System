# -*- coding: utf-8 -*-

from views.UI_DbsTableSelect import Ui_DbsTableSelect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from libs import dbsConnector


class DbsTableSelect(QWidget, Ui_DbsTableSelect):
    backSignal = pyqtSignal()

    def __init__(self, conf, parent=None):
        super(DbsTableSelect, self).__init__(parent)
        self.setupUi(self)
        self.conf = conf
        self.mydb = dbsConnector('mysql', self.conf)
        self.tables_df = self.getTableNames()
        self.tables = list(self.tables_df.columns)
        for table in self.tables:
            self.tableNamesWidget.addItem(table)

    def getTableNames(self):
        tables_df = self.mydb.read_sql("SHOW TABLES")

        return tables_df

    def backClicked(self):
        self.backSignal.emit()

    def tableSelected(self, clicked_item):
        print(clicked_item.text())
