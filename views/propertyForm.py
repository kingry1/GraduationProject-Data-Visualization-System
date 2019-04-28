# -*- coding: utf-8 -*-

from .UI_propertyForm import Ui_propertyForm
from PyQt5.QtWidgets import QWidget, QColorDialog


class propertyForm(QWidget, Ui_propertyForm):
    def __init__(self, parent=None):
        super(propertyForm, self).__init__(parent)
        self.setupUi(self)
        self.rgb = None

    def color_pallet(self):
        self.rgb = QColorDialog.getColor()
        r, g, b, a = self.rgb.getRgb()
        rgb_string = "{}, {}, {}, {}".format(r, g, b, a)
        self.lineEdit_color.setText(rgb_string)

    def set_content_enable(self):
        self.lineEdit_label_content.setEnabled(True)

    def content_clicked(self):
        self.lineEdit_label_content.setEnabled(False)
