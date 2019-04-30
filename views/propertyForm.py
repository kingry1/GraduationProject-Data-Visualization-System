# -*- coding: utf-8 -*-

from .UI_propertyForm import Ui_propertyForm
from PyQt5.QtWidgets import QWidget, QColorDialog
from PyQt5.QtGui import QColor


class propertyForm(QWidget, Ui_propertyForm):
    def __init__(self, parent=None):
        super(propertyForm, self).__init__(parent)
        self.setupUi(self)
        self.rgb = QColor(100, 100, 255)
        self.lineEdit_color.setStyleSheet('background-color: rgba({})'.format(self.get_rgb_string(self.rgb)))

    def color_pallet(self):
        self.rgb = QColorDialog.getColor()
        rgb_string = self.get_rgb_string(self.rgb)
        self.lineEdit_color.setStyleSheet('background-color: rgba({})'.format(rgb_string))

    def set_content_enable(self):
        self.lineEdit_label_content.setEnabled(True)

    def content_clicked(self):
        self.lineEdit_label_content.setEnabled(False)

    @staticmethod
    def get_rgb_string(color_object):
        r, g, b, a = color_object.getRgb()
        rgb_string = "{}, {}, {}, {}".format(r, g, b, a)

        return rgb_string
