# -*- coding: utf-8 -*-

from .UI_styleForm import Ui_styleForm
from PyQt5.QtWidgets import QWidget, QColorDialog
from PyQt5.QtGui import QColor


class styleForm(QWidget, Ui_styleForm):
    def __init__(self, parent=None):
        super(styleForm, self).__init__(parent)
        self.setupUi(self)
        self.title_color = QColor(100, 100, 255)
        self.background_color = QColor(255, 255, 255)
        self.lineEdit_title_color.setStyleSheet(
            'background-color: rgba({})'.format(self.get_rgb_string(self.title_color)))
        self.lineEdit_background_color.setStyleSheet(
            'background-color: rgba({})'.format(self.get_rgb_string(self.background_color)))

    def title_color_pallet(self):
        self.title_color = QColorDialog.getColor()
        rgb_string = self.get_rgb_string(self.title_color)
        self.lineEdit_title_color.setStyleSheet('background-color: rgba({})'.format(rgb_string))

    def background_color_pallet(self):
        self.background_color = QColorDialog.getColor()
        rgb_string = self.get_rgb_string(self.background_color)
        self.lineEdit_background_color.setStyleSheet(
            'background-color: rgba({})'.format(rgb_string))

    def set_title_content_enable(self):
        self.lineEdit_title_content.setEnabled(True)

    def title_content_clicked(self):
        self.lineEdit_title_content.setEnabled(False)

    @staticmethod
    def get_rgb_string(color_object):
        r, g, b, a = color_object.getRgb()
        rgb_string = "{}, {}, {}, {}".format(r, g, b, a)

        return rgb_string
