# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from GUIs.MainDbsConfWin import MainDbsConfWin
from GUIs.DbsTableSelect import DbsTableSelect
from libs import GL


class Controller(QObject):
    def __init__(self):
        super(Controller, self).__init__()

    def init_main(self):
        self.mainDbsConf = MainDbsConfWin()
        self.mainDbsConf.callDbsTableSignal.connect(self.show_table_select)
        self.mainDbsConf.show()

    def show_table_select(self, dic):
        self.tableSelect = DbsTableSelect(dic)
        self.tableSelect.backSignal.connect(self.show_main)
        self.mainDbsConf.close()
        self.tableSelect.show()

    def show_main(self):
        GL.refresh_conf()
        self.mainDbsConf = MainDbsConfWin()
        self.mainDbsConf.callDbsTableSignal.connect(self.show_table_select)
        self.tableSelect.close()
        self.mainDbsConf.show()
