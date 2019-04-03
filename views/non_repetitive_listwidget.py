# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QListWidget
from PyQt5.QtGui import QStandardItemModel
from PyQt5 import QtCore


class Non_repetitive_ListWidget(QListWidget):
    def __init__(self, parent=None):
        super(Non_repetitive_ListWidget, self).__init__(parent)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        source_item = QStandardItemModel()
        source_item.dropMimeData(data, QtCore.Qt.CopyAction, 0, 0, QtCore.QModelIndex())
        print(source_item.item(0, 0).text())


def dropEvent(self, e):
        self.addItem(e.mimeData().text())
