from PyQt5.QtCore import QThread, pyqtSignal
import pandas as pd
from libs import GL, dbsConnector


class ShowTablesThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, conf, table_name):
        super(ShowTablesThread, self).__init__()
        self.conf = conf
        self.table_name = table_name
        self.mydb = None

    def run(self):
        sql = "SELECT * FROM {0}.{1}".format(self.conf['name'], self.table_name)
        self.mydb = dbsConnector(self.conf)
        GL.tables_df = self.mydb.read_sql(sql_cmd=sql)

        self.trigger.emit()
