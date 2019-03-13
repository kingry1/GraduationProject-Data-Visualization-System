# -*- coding: utf-8 -*-

import mysql.connector
import pandas as pd


class DbsConnector:
    def __init__(self, conf):
        self.conf = conf
        self.host = conf['host']
        self.port = conf['port']
        self.user = conf['user']
        self.password = conf['password']
        self.db = conf['name']

        if self.conf['type'] == 'mysql':
            try:
                self.mydb = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                    db=self.db
                )
            except mysql.connector.Error as err:
                print(err)

    def read_sql(self, sql_cmd):
        df = ''
        try:
            df = pd.read_sql(sql=sql_cmd, con=self.mydb)
        except Exception as err:
            print(err)
        return df

    def driver_mysql(self, sql_cmd):
        results = ''
        try:
            myCursor = self.mydb.cursor()
            myCursor.execute(sql_cmd)
            results = myCursor.fetchall()
        except mysql.connector.Error as err:
            print(err)

        return results
