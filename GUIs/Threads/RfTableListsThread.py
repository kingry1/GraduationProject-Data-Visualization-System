from PyQt5.QtCore import QThread, pyqtSignal
import pandas as pd
from libs import GL, dbsConnector


class RfTableListsThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, conf):
        super(RfTableListsThread, self).__init__()
        self.conf = conf
        self.mydb = None

    def run(self):
        sql = "SHOW TABLES;".format(self.conf['name'])
        self.mydb = dbsConnector(self.conf)
        GL.tables_df = self.mydb.driver_mysql(sql_cmd=sql)

        self.trigger.emit()
