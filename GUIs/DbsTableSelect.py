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
        self.mydb = dbsConnector(self.conf)
        self.tables_raw = self.getTableNames()

        for table in self.tables_raw:
            self.tableNamesWidget.addItem(table[0])

    def getTableNames(self):
        sql = "SHOW TABLES;".format(self.conf['name'])
        tables_df = self.mydb.driver_mysql(sql_cmd=sql)

        return tables_df

    def backClicked(self):
        self.backSignal.emit()

    def tableSelected(self, clicked_item):
        print(clicked_item.text())
