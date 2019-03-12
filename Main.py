# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from GUIs.MainDbsConfWin import MainDbsConfWin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainDbsConfWin()
    myWin.show()
    sys.exit(app.exec_())
