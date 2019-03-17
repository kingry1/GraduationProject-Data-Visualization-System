# -*- coding: utf-8 -*-

import mysql.connector

# from mysql.connector.errors import DatabaseError

try:
    # 接收参数：user, password, host, port=3306, unix_socket and database
    # 返回一个MySQLConnection Object
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sjn19970508',
        database='runoob_db'
    )

    # 创建一个查询
    myCursor = mydb.cursor()

    myCursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
except mysql.connector.Error as err:
    print(err)
