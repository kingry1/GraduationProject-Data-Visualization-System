# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from libs import GL
from libs.DdbsConnector import DbsConnector as dbsConnector


class RfTableListsThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, conf):
        super(RfTableListsThread, self).__init__()
        self.conf = conf
        self.mydb = None

    def run(self):
        self.mydb = dbsConnector(self.conf)
        GL.tables_lists = self.mydb.get_table_names()

        self.trigger.emit()
