# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class ClickableLabel(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.if_mouse_press = False

    def mousePressEvent(self, e):
        self.clicked.emit(self.objectName())

    def unclick(self):
        self.setStyleSheet('border-width: 0px;')
        self.if_mouse_press = False

    def click(self):
        self.if_mouse_press = True
        self.setStyleSheet(
            'border-style: dashed; border-width: 1px; border-color: rgb(128, 128, 128); padding: -1px;')
