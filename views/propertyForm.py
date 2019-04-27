# -*- coding: utf-8 -*-

from .UI_propertyForm import Ui_propertyForm
from PyQt5.QtWidgets import QWidget, QColorDialog


class propertyForm(QWidget, Ui_propertyForm):
    def __init__(self, parent=None):
        super(propertyForm, self).__init__(parent)
        self.setupUi(self)

    def color_pallet(self):
        self.rgb = QColorDialog.getColor()
        r, g, b, a = self.rgb.getRgb()
        rgb_string = "{}, {}, {}".format(r, g, b)
        self.lineEdit_color.setText(rgb_string)
