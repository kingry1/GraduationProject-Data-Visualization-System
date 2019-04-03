# -*- coding: utf-8 -*-

from views.UI_DataVisualizationWin import Ui_DataVisualizationWin
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from libs import GL
from pandas.api.types import *
from views.clickablelabel import ClickableLabel


class DataVisualizationWin(QMainWindow, Ui_DataVisualizationWin):
    backSignal = pyqtSignal(dict)

    def __init__(self, conf, table_name, parent=None):
        super(DataVisualizationWin, self).__init__(parent)
        self.setupUi(self)
        self.conf = conf
        self.table_name = table_name
        print('conf:', self.conf)
        print('table_name:', self.table_name)
        for index in list(GL.tables_df.dtypes.index):
            data_type = GL.tables_df.dtypes[index]
            if is_object_dtype(data_type) or is_datetime64_any_dtype(data_type):
                self.listWidget_dimension.addItem(index)
            else:
                self.listWidget_indicator.addItem(index)
        self.clicked_graph_type_label = {}

    def backClicked(self):
        self.backSignal.emit(self.conf)

    def horizontalParamRemove(self, clicked_item):
        # 删除
        text = clicked_item.text()
        print(text)

    def verticalParamRemove(self, clicked_item):
        # 删除
        text = clicked_item.text()
        print(text)

    def graphTypeClicked(self, clicked_item_name):
        clicked_item = self.widget_graph.findChild(ClickableLabel, clicked_item_name)
        self.clicked_graph_type_label[clicked_item_name] = clicked_item
        for label in self.clicked_graph_type_label.values():
            label.unclick()
        clicked_item.click()
        self.generateButton.setEnabled(True)

    def get_clicked_graph_name(self):
        clicked_name = None
        for label in self.clicked_graph_type_label.values():
            if label.if_mouse_press:
                clicked_name = label.objectName()
                break
        return clicked_name

    def generateGraph(self):
        print(self.get_clicked_graph_name())
        self.mplwidget.plot()
