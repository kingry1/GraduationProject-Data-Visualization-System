# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DbsTableSelect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DbsTableSelect(object):
    def setupUi(self, DbsTableSelect):
        DbsTableSelect.setObjectName("DbsTableSelect")
        DbsTableSelect.resize(438, 329)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DbsTableSelect)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DbsTableSelect)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(DbsTableSelect)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DbsTableSelect)
        QtCore.QMetaObject.connectSlotsByName(DbsTableSelect)

    def retranslateUi(self, DbsTableSelect):
        _translate = QtCore.QCoreApplication.translate
        DbsTableSelect.setWindowTitle(_translate("DbsTableSelect", "数据表选择"))
        self.label.setText(_translate("DbsTableSelect", "Second Screen"))
        self.pushButton.setText(_translate("DbsTableSelect", "EXIT"))

