# -*- coding: utf-8 -*-

from views.UI_DataVisualizationWin import Ui_DataVisualizationWin
from PyQt5.QtWidgets import QMainWindow


class DataVisualizationWin(QMainWindow, Ui_DataVisualizationWin):
    def __init__(self, conf, table_name, parent=None):
        super(DataVisualizationWin, self).__init__(parent)
        self.setupUi(self)
        self.conf = conf
        self.table_name = table_name
        print('conf:', self.conf)
        print('table_name:', self.table_name)
