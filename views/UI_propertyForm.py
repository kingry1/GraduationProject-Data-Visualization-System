# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_propertyForm.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_propertyForm(object):
    def setupUi(self, propertyForm):
        propertyForm.setObjectName("propertyForm")
        propertyForm.resize(256, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(propertyForm)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(propertyForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(250, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.toolBox.setObjectName("toolBox")
        self.page_color = QtWidgets.QWidget()
        self.page_color.setGeometry(QtCore.QRect(0, 0, 250, 181))
        self.page_color.setObjectName("page_color")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_color)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_color = QtWidgets.QLineEdit(self.page_color)
        self.lineEdit_color.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_color.sizePolicy().hasHeightForWidth())
        self.lineEdit_color.setSizePolicy(sizePolicy)
        self.lineEdit_color.setObjectName("lineEdit_color")
        self.gridLayout.addWidget(self.lineEdit_color, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.page_color)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.page_color)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.toolBox.addItem(self.page_color, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 230, 181))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 230, 181))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(propertyForm)
        self.toolBox.setCurrentIndex(0)
        self.pushButton.clicked.connect(propertyForm.color_pallet)
        QtCore.QMetaObject.connectSlotsByName(propertyForm)

    def retranslateUi(self, propertyForm):
        _translate = QtCore.QCoreApplication.translate
        propertyForm.setWindowTitle(_translate("propertyForm", "Form"))
        self.label.setText(_translate("propertyForm", "R,G,B"))
        self.pushButton.setText(_translate("propertyForm", "调色板"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_color), _translate("propertyForm", "颜色"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("propertyForm", "Page 2"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("propertyForm", "Page 3"))


