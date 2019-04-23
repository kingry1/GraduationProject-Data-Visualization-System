# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from libs import GL
from libs.DdbsConnector import DbsConnector as dbsConnector


class VisualizationDataThread(QThread):
    trigger = pyqtSignal()
    fail = pyqtSignal(str)

    def __init__(self, conf, table_name, horizontal_axes, vertical_axes, graph_type):
        super(VisualizationDataThread, self).__init__()
        self.horizontal_axes = horizontal_axes
        self.vertical_axes = vertical_axes
        self.graph_type = graph_type[6:]
        self.conf = conf
        self.table_name = table_name
        self.mydb = None

    def run(self):
        self.mydb = dbsConnector(self.conf)
        sql = None
        if self.graph_type == "line_chart":
            sql_front = "SELECT "
            for zongzhou in self.vertical_axes:
                if zongzhou == 'count(*)':
                    sql_front = sql_front + ', '
                else:
                    sql_front = sql_front + "sum({})".format(zongzhou) + ', '
            sql_front = sql_front + self.horizontal_axes[0] + ', '
            sql_front = sql_front[:-2]
            sql_middle = " FROM {}".format(self.table_name)
            sql_end = " GROUP BY {};".format(self.horizontal_axes[0])
            sql = sql_front + sql_middle + sql_end
        elif self.graph_type == "histogram":
            if len(self.vertical_axes) > 0:
                sql_front = "SELECT "
                for zhibiao in self.horizontal_axes:
                    if zhibiao == 'count(*)':
                        sql_front = sql_front + zhibiao + ', '
                    else:
                        sql_front = sql_front + "sum({})".format(zhibiao) + ', '
                sql_front = sql_front[:-2]
                sql_middle = " FROM {}".format(self.table_name)
                sql_end = " GROUP BY {};".format(self.vertical_axes[0])
                sql = sql_front + sql_middle + sql_end
            else:
                sql_front = "SELECT "
                for zhibiao in self.horizontal_axes:
                    sql_front = sql_front + zhibiao + ', '
                sql_front = sql_front[:-2]
                sql_middle = " FROM {};".format(self.table_name)
                sql = sql_front + sql_middle
        elif self.graph_type == "pie_chart":
            sql_front = "SELECT "
            for jiaodu in self.horizontal_axes:
                if jiaodu == 'count(*)':
                    sql_front = sql_front + jiaodu + ', '
                else:
                    sql_front = sql_front + "sum({})".format(jiaodu) + ', '
            sql_front = sql_front + self.vertical_axes[0] + ', '
            sql_front = sql_front[:-2]
            sql_middle = " FROM {}".format(self.table_name)
            sql_end = " GROUP BY {};".format(self.vertical_axes[0])
            sql = sql_front + sql_middle + sql_end
        try:
            GL.visualization_df = self.mydb.read_sql(sql_cmd=sql)
        except Exception as e:
            self.fail.emit(str(e))
            return
        finally:
            self.mydb.close_connection()

        self.trigger.emit()
