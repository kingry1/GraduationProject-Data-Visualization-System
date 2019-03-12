# -*- coding: utf-8 -*-

from views.UI_DbsTableSelect import Ui_DbsTableSelect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem, QInputDialog


class DbsTableSelect(QWidget, Ui_DbsTableSelect):
    def __init__(self, parent=None):
        super(DbsTableSelect, self).__init__(parent)
        self.setupUi(self)
