# -*- coding: utf-8 -*-

import mysql.connector
# from mysql.connector.errors import DatabaseError

try:
    # 接收参数：user, password, host, port=3306, unix_socket and database
    # 返回一个MySQLConnection Object
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sjn19970508'
    )

    # 创建一个查询
    myCursor = mydb.cursor()
    #
    # # 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
    # myCursor.execute("select * from city")
    # # 可以使用fetchall()，获取所有的查询结果集，返回值为一个tuple，每一个元素是一个list
    # res = myCursor.fetchall()
    # print(res)

    myCursor.execute("SHOW DATABASES")
except mysql.connector.Error as err:
    print(err)

result = myCursor.fetchmany(size=2)

for db in result:
    print(db)

mydb.close()
