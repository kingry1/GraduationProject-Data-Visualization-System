# -*- coding: utf-8 -*-

import mysql.connector
# from mysql.connector.errors import DatabaseError

# 导入matplotlib模块并使用Qt5Agg
import matplotlib

matplotlib.use('Qt5Agg')
# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets, QtGui
import matplotlib.pyplot as plt
import sys


class My_Main_window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # 父类初始化方法
        super(My_Main_window, self).__init__(parent)

        # 几个QWidgets
        self.figure = plt.figure()
        self.canvas = MatplotlibCanvas()
        self.button_plot = QtWidgets.QPushButton("绘制")

        # 连接事件
        self.button_plot.clicked.connect(self.canvas.plot)

        # 设置布局
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.button_plot)
        self.setLayout(layout)


class MatplotlibCanvas(FigureCanvas):
    def __init__(self):
        self.figure = plt.figure()
        super(MatplotlibCanvas, self).__init__(self.figure)

    def plot(self):
        try:
            # 接收参数：user, password, host, port=3306, unix_socket and database
            # 返回一个MySQLConnection Object
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Sjn19970508'
            )

            # 创建一个查询
            myCursor = mydb.cursor()
            #
            # # 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
            # myCursor.execute("select * from city")
            # # 可以使用fetchall()，获取所有的查询结果集，返回值为一个tuple，每一个元素是一个list
            # res = myCursor.fetchall()
            # print(res)

            myCursor.execute("SELECT COUNT(*), country FROM sakila.customer_list GROUP BY country;")
        except mysql.connector.Error as err:
            print(err)

        results = myCursor.fetchall()

        output = {}

        for (number, country) in results:
            output[country] = number

        mydb.close()

        print(output)

        num = 4
        ax = self.figure.add_subplot(111)
        ax.bar(list(output.keys())[0:num], list(output.values())[0:num], align='center', color='steelblue', alpha=0.8)
        ax.set_ylabel(u'Count')
        ax.set_title(u'PyQt5 + Matplotlib')
        self.draw()

# 运行程序
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()
