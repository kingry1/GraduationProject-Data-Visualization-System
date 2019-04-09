# -*- coding: utf-8 -*-

from .UI_propertyForm import Ui_propertyForm
from PyQt5.QtWidgets import QWidget


class propertyForm(QWidget, Ui_propertyForm):
    def __init__(self, parent=None):
        super(propertyForm, self).__init__(parent)
        self.setupUi(self)
