# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DataVisualizationWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataVisualizationWin(object):
    def setupUi(self, DataVisualizationWin):
        DataVisualizationWin.setObjectName("DataVisualizationWin")
        DataVisualizationWin.resize(926, 689)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataVisualizationWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DataVisualizationWin)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_win = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_win.setObjectName("horizontalLayout_win")
        self.horizontalLayout_main = QtWidgets.QVBoxLayout()
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.horizontalLayout_UI = QtWidgets.QHBoxLayout()
        self.horizontalLayout_UI.setObjectName("horizontalLayout_UI")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setBaseSize(QtCore.QSize(0, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignVCenter)
        self.listWidget_dimension = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_dimension.sizePolicy().hasHeightForWidth())
        self.listWidget_dimension.setSizePolicy(sizePolicy)
        self.listWidget_dimension.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget_dimension.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget_dimension.setBaseSize(QtCore.QSize(0, 0))
        self.listWidget_dimension.setObjectName("listWidget_dimension")
        self.verticalLayout_6.addWidget(self.listWidget_dimension)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3, 0, QtCore.Qt.AlignVCenter)
        self.listWidget_indicator = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_indicator.sizePolicy().hasHeightForWidth())
        self.listWidget_indicator.setSizePolicy(sizePolicy)
        self.listWidget_indicator.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget_indicator.setObjectName("listWidget_indicator")
        self.verticalLayout_7.addWidget(self.listWidget_indicator)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_UI.addLayout(self.verticalLayout_3)
        self.verticalLayout_71 = QtWidgets.QVBoxLayout()
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 0))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_71.addLayout(self.verticalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_71.addWidget(self.line_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.property_tab = QtWidgets.QWidget()
        self.property_tab.setObjectName("property_tab")
        self.tabWidget.addTab(self.property_tab, "")
        self.style_tab = QtWidgets.QWidget()
        self.style_tab.setObjectName("style_tab")
        self.tabWidget.addTab(self.style_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_71.addLayout(self.verticalLayout_4)
        self.horizontalLayout_UI.addLayout(self.verticalLayout_71)
        self.verticalLayout_61 = QtWidgets.QVBoxLayout()
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_4.sizePolicy().hasHeightForWidth())
        self.listWidget_4.setSizePolicy(sizePolicy)
        self.listWidget_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.listWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_4.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_4.setObjectName("listWidget_4")
        self.horizontalLayout_4.addWidget(self.listWidget_4)
        self.verticalLayout_61.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_3.sizePolicy().hasHeightForWidth())
        self.listWidget_3.setSizePolicy(sizePolicy)
        self.listWidget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.listWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_3.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_3.setObjectName("listWidget_3")
        self.horizontalLayout_3.addWidget(self.listWidget_3)
        self.verticalLayout_61.addLayout(self.horizontalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_61.addWidget(self.line_4)
        self.widget = MplWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_61.addWidget(self.widget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_61.addLayout(self.horizontalLayout_5)
        self.verticalLayout_61.setStretch(3, 1)
        self.horizontalLayout_UI.addLayout(self.verticalLayout_61)
        self.horizontalLayout_UI.setStretch(2, 1)
        self.horizontalLayout_main.addLayout(self.horizontalLayout_UI)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_main.addLayout(self.horizontalLayout)
        self.horizontalLayout_win.addLayout(self.horizontalLayout_main)
        DataVisualizationWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataVisualizationWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 22))
        self.menubar.setObjectName("menubar")
        DataVisualizationWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataVisualizationWin)
        self.statusbar.setObjectName("statusbar")
        DataVisualizationWin.setStatusBar(self.statusbar)

        self.retranslateUi(DataVisualizationWin)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.widget.plot)
        self.pushButton_2.clicked.connect(DataVisualizationWin.backClicked)
        QtCore.QMetaObject.connectSlotsByName(DataVisualizationWin)

    def retranslateUi(self, DataVisualizationWin):
        _translate = QtCore.QCoreApplication.translate
        DataVisualizationWin.setWindowTitle(_translate("DataVisualizationWin", "数据可视化"))
        self.label.setText(_translate("DataVisualizationWin", "表名称"))
        self.label_2.setText(_translate("DataVisualizationWin", "维度"))
        self.label_3.setText(_translate("DataVisualizationWin", "指标"))
        self.label_4.setText(_translate("DataVisualizationWin", "图表类型"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.property_tab), _translate("DataVisualizationWin", "图形属性"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.style_tab), _translate("DataVisualizationWin", "组件样式"))
        self.label_6.setText(_translate("DataVisualizationWin", "横轴"))
        self.label_5.setText(_translate("DataVisualizationWin", "纵轴"))
        self.pushButton.setText(_translate("DataVisualizationWin", "生成图表"))
        self.pushButton_2.setText(_translate("DataVisualizationWin", "返回"))

from .mplwidget import MplWidget
