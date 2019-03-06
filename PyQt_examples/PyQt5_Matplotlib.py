# coding:utf-8

# 导入matplotlib模块并使用Qt5Agg
import matplotlib

matplotlib.use('Qt5Agg')
# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
import matplotlib.pyplot as plt
import sys


class My_Main_window(QWidget):
    def __init__(self, parent=None):
        # 父类初始化方法
        super(My_Main_window, self).__init__(parent)

        # 几个QWidgets
        self.figure = plt.figure()
        self.canvas = MatplotlibCanvas()
        self.button_plot = QPushButton("绘制")

        # 连接事件
        self.button_plot.clicked.connect(self.canvas.plot)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.button_plot)
        self.setLayout(layout)


class MatplotlibCanvas(FigureCanvas):
    def __init__(self):
        self.figure = plt.figure()
        super(MatplotlibCanvas, self).__init__(self.figure)

    def plot(self):
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([1, 2, 3, 4, 5])
        self.draw()

# 运行程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()
