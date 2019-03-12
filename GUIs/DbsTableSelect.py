# -*- coding: utf-8 -*-

from views.UI_DbsTableSelect import Ui_DbsTableSelect
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QInputDialog
from PyQt5.QtCore import pyqtSignal


class DbsTableSelect(QWidget, Ui_DbsTableSelect):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(DbsTableSelect, self).__init__(parent)
        self.setupUi(self)

    def backClicked(self):
        self.backSignal.emit()
