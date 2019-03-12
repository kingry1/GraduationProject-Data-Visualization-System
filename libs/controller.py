# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from GUIs.MainDbsConfWin import MainDbsConfWin
from GUIs.DbsTableSelect import DbsTableSelect


class Controller(QObject):
    def __init__(self):
        super(Controller, self).__init__()

    def init_main(self):
        self.mainDbsConf = MainDbsConfWin()
        self.mainDbsConf.callDbsTableSignal.connect(self.show_table_select)
        self.mainDbsConf.show()

    def show_table_select(self):
        self.tableSelect = DbsTableSelect()
        self.tableSelect.backSignal.connect(self.show_main)
        self.mainDbsConf.close()
        self.tableSelect.show()

    def show_main(self):
        self.mainDbsConf = MainDbsConfWin()
        self.mainDbsConf.callDbsTableSignal.connect(self.show_table_select)
        self.tableSelect.close()
        self.mainDbsConf.show()
