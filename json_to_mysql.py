# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import xlrd

df = pd.read_json('test.json')
print(df.index)
engine = create_engine('mysql+mysqlconnector://root:Sjn19970508@localhost:3306/sakila')
df.to_sql(name='three', con=engine, if_exists='append', index=False)
