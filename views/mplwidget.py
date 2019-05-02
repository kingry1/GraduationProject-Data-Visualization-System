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
            dataframe.set_index([horizontal for horizontal in horizontal_axes], inplace=True)
            dataframe.plot.line(ax=ax, linewidth=graph_conf['property']['line_width'], color=graph_conf['property']['line_color'].name())
            ax.set_title(label='' if graph_conf['style']['title_enabled'] == 'no' else graph_conf['style']['title_content'], color=graph_conf['style']['title_color'].name())
            ax.patch.set_facecolor(graph_conf['style']['background_color'].name())
        elif graph_type == 'histogram':
            dataframe.plot.hist(ax=ax, color=graph_conf['property']['line_color'].name(), width=graph_conf['property']['line_width'])
            ax.set_title(label='' if graph_conf['style']['title_enabled'] == 'no' else graph_conf['style']['title_content'], color=graph_conf['style']['title_color'].name())
            ax.patch.set_facecolor(graph_conf['style']['background_color'].name())
        elif graph_type == 'pie_chart':
            dataframe.set_index([vertical for vertical in vertical_axes], inplace=True)
            dataframe.plot.pie(ax=ax, subplots=True, color=graph_conf['property']['line_color'].name())
            ax.set_title(label='' if graph_conf['style']['title_enabled'] == 'no' else graph_conf['style']['title_content'], color=graph_conf['style']['title_color'].name())
            ax.patch.set_facecolor(graph_conf['style']['background_color'].name())
        ax.legend(loc=graph_conf['style']['legend_position'])
        # legend
        if graph_conf['style']['legend_enabled'] == 'no':
            ax.legend_.remove()
        self.canvas.draw()

    def save(self, filename):
        self.figure.savefig('./{}'.format(filename))
