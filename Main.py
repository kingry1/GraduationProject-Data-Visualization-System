# -*- coding: utf-8 -*-

import sys
from libs.controller import Controller
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Controller()
    myWin.init_main()
    sys.exit(app.exec_())
