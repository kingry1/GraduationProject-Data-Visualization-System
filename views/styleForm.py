# -*- coding: utf-8 -*-

from .UI_styleForm import Ui_styleForm
from PyQt5.QtWidgets import QWidget, QColorDialog


class styleForm(QWidget, Ui_styleForm):
    def __init__(self, parent=None):
        super(styleForm, self).__init__(parent)
        self.setupUi(self)
        self.title_color = None
        self.background_color = None

    def title_color_pallet(self):
        self.title_color = QColorDialog.getColor()
        r, g, b, a = self.title_color.getRgb()
        rgb_string = "{}, {}, {}, {}".format(r, g, b, a)
        self.lineEdit_title_color.setStyleSheet('background-color: rgba({})'.format(rgb_string))

    def background_color_pallet(self):
        self.background_color = QColorDialog.getColor()
        r, g, b, a = self.background_color.getRgb()
        rgb_string = "{}, {}, {}, {}".format(r, g, b, a)
        self.lineEdit_background_color.setStyleSheet('background-color: rgba({})'.format(rgb_string))

    def set_title_content_enable(self):
        self.lineEdit_title_content.setEnabled(True)

    def title_content_clicked(self):
        self.lineEdit_title_content.setEnabled(False)
