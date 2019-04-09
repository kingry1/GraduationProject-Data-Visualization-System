# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertyForm.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_propertyForm(object):
    def setupUi(self, propertyForm):
        propertyForm.setObjectName("propertyForm")
        propertyForm.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(propertyForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(propertyForm)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(propertyForm)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(propertyForm)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(propertyForm)
        QtCore.QMetaObject.connectSlotsByName(propertyForm)

    def retranslateUi(self, propertyForm):
        _translate = QtCore.QCoreApplication.translate
        propertyForm.setWindowTitle(_translate("propertyForm", "Form"))
        self.pushButton.setText(_translate("propertyForm", "PushButton"))
        self.pushButton_3.setText(_translate("propertyForm", "PushButton"))
        self.pushButton_2.setText(_translate("propertyForm", "PushButton"))


