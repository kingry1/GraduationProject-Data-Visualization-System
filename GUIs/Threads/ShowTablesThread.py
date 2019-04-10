# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from libs import GL
from libs.DdbsConnector import DbsConnector as dbsConnector


class ShowTablesThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, conf, table_name):
        super(ShowTablesThread, self).__init__()
        self.conf = conf
        self.table_name = table_name
        self.mydb = None

    def run(self):
        self.mydb = dbsConnector(self.conf)
        GL.tables_df = self.mydb.get_table_content(table_name=self.table_name)

        self.trigger.emit()
