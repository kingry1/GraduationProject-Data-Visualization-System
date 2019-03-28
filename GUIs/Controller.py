# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from GUIs.MainDbsConfWin import MainDbsConfWin
from GUIs.DbsTableSelect import DbsTableSelect
from GUIs.DataVisualizationWin import DataVisualizationWin
from libs import GL


class Controller(QObject):
    def __init__(self):
        super(Controller, self).__init__()
        self.mainDbsConf = None
        self.tableSelect = None
        self.dataVisualization = None

    def init_main(self):
        self.mainDbsConf = MainDbsConfWin()
        self.mainDbsConf.callDbsTableSignal.connect(self.show_table_select)
        self.mainDbsConf.show()

    def show_table_select(self, dic):
        self.tableSelect = DbsTableSelect(dic)
        self.tableSelect.backSignal.connect(self.back_main)
        self.tableSelect.visualizationSignal.connect(self.show_data_visualization)
        self.mainDbsConf.close()
        self.tableSelect.show()

    def back_main(self):
        GL.refresh_conf()
        self.mainDbsConf = MainDbsConfWin()
        self.mainDbsConf.callDbsTableSignal.connect(self.show_table_select)
        self.tableSelect.close()
        self.mainDbsConf.show()

    def show_data_visualization(self, conf, table_name):
        self.dataVisualization = DataVisualizationWin(conf=conf, table_name=table_name)
        # 连接返回信号
        self.dataVisualization.backSignal.connect(self.back_table_select)
        self.tableSelect.close()
        self.dataVisualization.show()

    def back_table_select(self, dic):
        self.tableSelect = DbsTableSelect(dic)
        self.tableSelect.backSignal.connect(self.back_main)
        self.tableSelect.visualizationSignal.connect(self.show_data_visualization)
        self.dataVisualization.close()
        self.tableSelect.show()
