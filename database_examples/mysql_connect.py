# -*- coding: utf-8 -*-

import mysql.connector

# 接收参数：user, password, host, port=3306, unix_socket and database
# 返回一个MySQLConnection Object
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sjn19970508',
    database='world'
)

# 创建一个查询
cmd = conn.cursor()

# 执行一条原生的SQL语句，执行结果保存在cmd中，没有返回值
cmd.execute("select * from city")
# 可以使用fetchall()，获取所有的查询结果集，返回值为一个tuple，每一个元素是一个list
res = cmd.fetchall()
print(res)