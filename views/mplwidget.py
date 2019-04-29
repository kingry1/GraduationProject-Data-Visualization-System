# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class MplWidget(QWidget):
    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)

    def plot(self, horizontal_axes, vertical_axes, graph_type, graph_conf, dataframe=None):
        # {'property': {'line_color': <PyQt5.QtGui.QColor object at 0x157d12828>, 'line_width': 1, 'label_content': ''}, 'style': {'title_color': None, 'title_content': '', 'title_enabled': '是', 'legend_position': '右', 'legend_enabled': '是', 'background_color': None}}
        self.figure.clear()
        graph_type = graph_type[6:]
        # ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax = self.figure.add_subplot(1, 1, 1)
        if graph_type == 'line_chart':
            # dataframe['count(*)'].plot(kind='line', ax=ax)
            dataframe.set_index([horizontal for horizontal in horizontal_axes], inplace=True)
            dataframe.plot.line(ax=ax, title=None if graph_conf['style']['title_enabled'] == 'no' else graph_conf['style']['title_content'], legend=False if graph_conf['style']['legend_enabled'] == 'no' else True)
        elif graph_type == 'histogram':
            dataframe.plot.hist(ax=ax, title=None if graph_conf['style']['title_enabled'] == 'no' else graph_conf['style']['title_content'], legend=False if graph_conf['style']['legend_enabled'] == 'no' else True)
        elif graph_type == 'pie_chart':
            dataframe.set_index([vertical for vertical in vertical_axes], inplace=True)
            dataframe.plot.pie(ax=ax, subplots=True, title=None if graph_conf['style']['title_enabled'] == 'no' else graph_conf['style']['title_content'], legend=False if graph_conf['style']['legend_enabled'] == 'no' else True)
        ax.legend(loc=graph_conf['style']['legend_position'])
        self.canvas.draw()

    def save(self, filename):
        self.figure.savefig('./{}'.format(filename))
