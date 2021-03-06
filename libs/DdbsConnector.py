# -*- coding: utf-8 -*-

import mysql.connector
import psycopg2
import pandas as pd
import platform
from sqlalchemy import create_engine

if platform.system() == "Windows":
    import pyodbc


class DbsConnector:
    def __init__(self, conf):
        self.conf = conf
        self.connection = self.create_connection()

    def create_connection(self):
        connection = None
        if self.conf['type'] == 'mysql':
            try:
                connection = mysql.connector.connect(
                    host=self.conf['host'],
                    user=self.conf['user'],
                    password=self.conf['password'],
                    port=self.conf['port'],
                    db=self.conf['name']
                )
            except mysql.connector.Error as err:
                print(err)
        elif self.conf['type'] == 'Access':
            try:
                MDB = self.conf['file_path']
                DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
                connection = pyodbc.connect('DRIVER={};DBQ={}'.format(DRV, MDB))
            except Exception as e:
                print(e)
        elif self.conf['type'] == 'postgresql':
            try:
                connection = psycopg2.connect(
                    host=self.conf['host'],
                    user=self.conf['user'],
                    password=self.conf['password'],
                    port=self.conf['port'],
                    dbname=self.conf['name']
                )
            except psycopg2.DatabaseError as err:
                print(err)
        return connection

    def read_sql(self, sql_cmd):
        df = ''
        try:
            df = pd.read_sql(sql=sql_cmd, con=self.connection)
        except Exception as err:
            raise err
        return df

    def driver_sql(self, sql_cmd):
        results = ''
        try:
            myCursor = self.connection.cursor()
            myCursor.execute(sql_cmd)
            results = myCursor.fetchall()
            myCursor.close()
        except mysql.connector.Error as err:
            print(err)
        except psycopg2.DatabaseError as err:
            print(err)

        return results

    def get_table_names(self):
        if self.conf['type'] == 'Access':
            cursor = self.connection.cursor()
            tables = cursor.tables(tableType='TABLE')
            table_names = [table.table_name for table in tables]
            return table_names
        elif self.conf['type'] == 'mysql':
            sql = "SHOW TABLES;"
            results_tuple = self.driver_sql(sql_cmd=sql)
            results = [result_tuple[0] for result_tuple in results_tuple]
            return results
        elif self.conf['type'] == 'postgresql':
            sql = "SELECT tablename FROM pg_tables WHERE schemaname = 'public';"
            results_tuple = self.driver_sql(sql_cmd=sql)
            results = [result_tuple[0] for result_tuple in results_tuple]
            return results

    def get_table_content(self, table_name):
        df = None
        if self.conf['type'] == 'Access':
            sql = "SELECT TOP 1000 * FROM {};".format(table_name)
            df = self.read_sql(sql_cmd=sql)
        elif self.conf['type'] == 'mysql':
            sql = "SELECT * FROM {0}.{1} LIMIT 1000;".format(self.conf['name'], table_name)
            df = self.read_sql(sql_cmd=sql)
        elif self.conf['type'] == 'postgresql':
            sql = "SELECT * FROM {0} LIMIT 1000;".format(table_name)
            df = self.read_sql(sql_cmd=sql)
        return df

    def close_connection(self):
        self.connection.close()

    @staticmethod
    def test_connection(conf):
        try:
            if conf['type'] == 'mysql':
                connection = mysql.connector.connect(
                    host=conf['host'],
                    user=conf['user'],
                    password=conf['password'],
                    port=conf['port'],
                    connect_timeout=1000
                )
                connection.close()
            elif conf['type'] == 'Access':
                MDB = conf['file_path']
                DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
                connection = pyodbc.connect('DRIVER={};DBQ={}'.format(DRV, MDB))
                connection.close()
            elif conf['type'] == 'postgresql':
                connection = psycopg2.connect(
                    host=conf['host'],
                    user=conf['user'],
                    password=conf['password'],
                    port=conf['port'],
                    connect_timeout=1000
                )
                connection.close()
        except mysql.connector.Error as err:
            raise err
        except pyodbc.Error as err:
            raise err
        except psycopg2.DatabaseError as err:
            raise err
        except Exception as err:
            raise err

    @staticmethod
    def add_excel(file_path, conf):
        file_without = '.'.join(file_path.split('/')[-1].split('.')[:-1])
        df = pd.read_excel(file_path)
        engine = create_engine(
            'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(conf['user'], conf['password'],
                                                           conf['host'], conf['port'],
                                                           conf['name']))
        df.to_sql(name=file_without, con=engine, if_exists='append')
        engine.dispose()

    @staticmethod
    def add_csv(file_path, conf):
        file_without = '.'.join(file_path.split('/')[-1].split('.')[:-1])
        df = pd.read_csv(file_path)
        engine = create_engine(
            'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(conf['user'], conf['password'],
                                                           conf['host'], conf['port'],
                                                           conf['name']))
        df.to_sql(name=file_without, con=engine, if_exists='append')
        engine.dispose()

    @staticmethod
    def add_json(file_path, conf):
        file_without = '.'.join(file_path.split('/')[-1].split('.')[:-1])
        df = pd.read_json(file_path)
        engine = create_engine(
            'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(conf['user'], conf['password'],
                                                           conf['host'], conf['port'],
                                                           conf['name']))
        df.to_sql(name=file_without, con=engine, if_exists='append', index=False)
        engine.dispose()
