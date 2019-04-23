# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector

try:
    # 接收参数：user, password, host, port=3306, unix_socket and database
    # 返回一个MySQLConnection Object
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sjn19970508'
    )
    sql_cmd = "USE sakila; SHOW TABLES"
    df = pd.read_sql(sql='SELECT sum(staff_id), payment_id FROM payment GROUP BY payment_id;', con=mydb)

except mysql.connector.Error as err:
    print(err)
#
# for (emp_no, salary) in myCursor:
#     print(emp_no)

mydb.close()
columns = list(df.columns)
print(columns)
for column in columns:
    print(df[column])
