# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainInit import Ui_MainWindow
from configparser import ConfigParser
import os

dirname = os.path.split(os.path.realpath(__file__))[0].replace('\\', '/')
dbConfFile = '/config/db.conf'
dbConfPath = dirname + dbConfFile


def config_dic(filename):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    dbsDic = {}
    db = {}
    sections = parser.sections()
    for section in sections:
        db = {}
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
            dbsDic[section] = db
    return dbsDic


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, dbs_dic, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.dbsDic = dbs_dic

    def slot1(self):
        for dbsName in self.dbsDic.keys():
            self.listWidget.addItem(dbsName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dic = config_dic(dbConfPath)
    print(dic)
    myWin = MyMainWindow(dbs_dic=dic)
    myWin.show()
    sys.exit(app.exec_())
