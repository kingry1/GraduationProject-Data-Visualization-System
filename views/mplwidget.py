# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


class MplWidget(QWidget):
    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.setLayout(vertical_layout)

    def plot(self):
        self.figure.clear()
        # ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax = self.figure.add_subplot(1, 1, 1)
        s = Series(np.random.randn(10).cumsum(), index=['a', 'b', 'c', 'd','e', 'f','g','h', 'i', 'j'])
        print(s)
        # s.plot(ax=axes[1])
        # index是横轴
        s.plot(kind='line', ax=ax)
        ax.set_ylabel('GDP')
        self.canvas.draw()

    def save(self, filename):
        self.figure.savefig('./{}'.format(filename))
