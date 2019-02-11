# -*- coding: utf-8 -*-

import pyodbc

workspace = 'C:/'


# Connection function to use for access
def Connection():
    MDB = '/'.join([workspace, 'srs2855_part1of2.accdb'])
    DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    return pyodbc.connect('DRIVER={};DBQ={}'.format(DRV, MDB))


def get_milk_data():
    conn = Connection()
    cursor = conn.cursor()
    sqlstring = 'SELECT TOP 100 * FROM assgn'
    output = cursor.execute(sqlstring)
    results = list(output)
    for result in results:
        print(result)



get_milk_data()