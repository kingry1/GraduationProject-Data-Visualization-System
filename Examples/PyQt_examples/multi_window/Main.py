# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_welcom import Ui_Main
from Ui_welcom2 import Ui_Main2


class Ui_Dialog(QtWidgets.QWidget, Ui_Main2):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)


# 主界面
class login(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)

    # 定义登录按钮的功能
    def loginEvent(self):
        self.hide()
        self.dia = Ui_Dialog()
        self.dia.show()


# 运行窗口Login
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    first = login()
    first.show()
    first.pushButton.clicked.connect(first.loginEvent)
    sys.exit(app.exec_())
