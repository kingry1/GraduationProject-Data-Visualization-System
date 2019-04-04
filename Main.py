# -*- coding: utf-8 -*-

import sys
from GUIs.Controller import Controller
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myWin = Controller()
    myWin.init_main()
    sys.exit(app.exec_())
