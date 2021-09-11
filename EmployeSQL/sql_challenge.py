# write python program to connect to postgres and load data to database
#
# conda install psycopg2 - PostgresSQL database adapter for Python
#
# https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/Winning_Numbers/lottotexas.csv
# Future - automate download and refresh numbers 
# 
#

import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load .env enviroment variables into the notebook
load_dotenv()
# Get the postgres connection information from os file. 


DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# print(DB_PASS)

conn = psycopg2.connect(dbname=DB_NAME, user = DB_USER, 
password = DB_PASS, host = DB_HOST)

sqlCreateTable = ("""create table lotto_stage (game_name char(15), draw_mon numeric(2,0),
draw_day numeric(2,0), draw_year numeric(4,0),num1 numeric(2,0), 
num2 numeric(2,0), num3 numeric(2,0),num4 numeric(2,0),num5 numeric(2,0),num6 numeric(2,0))""")

cur = conn.cursor()
cur.execute('drop table if exists lotto_stage')
cur.execute(sqlCreateTable)
conn.commit()




tx_lotto_data = 'https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/Winning_Numbers/lottotexas.csv'

cols = ['game_name','draw_mon','draw_day','draw_year','num1','num2','num3','num4','num5','num6']

df = pd.read_csv(tx_lotto_data,names = cols)

# sqlachemy

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/lotto')

# load df to database
df.to_sql('lotto_stage',engine,index=False,if_exists='replace')

# create tx_lotto table and combine date into date column

sqlCreateTable = ("""create table tx_lotto (game_date date, num1 numeric(2,0), 
num2 numeric(2,0), num3 numeric(2,0),num4 numeric(2,0),num5 numeric(2,0),num6 numeric(2,0))""")

cur = conn.cursor()
cur.execute('drop table if exists tx_lotto')
cur.execute(sqlCreateTable)
conn.commit()

cur.execute ('truncate table tx_lotto;')
conn.commit()
sql = f'''
INSERT INTO tx_lotto 
(game_date,num1,num2,num3,num4,num5,num6) 
SELECT '{draw_year}-{draw_mon}-{draw_day}'
,num1
,num2
,num3
,num4
,num5
,num6 FROM lotto_stage
'''
sqlMergeData = 'insert into tx_lotto (game_date,num1,num2,num3,num4,num5,num6) \
select format (''''%s-%s-%s'''', draw_year,draw_mon,draw_day)::date, \
		num1,num2,num3,num4,num5,num6 from lotto_stage;'

cur.execute(sqlMergeData)
conn.commit()


print ('connection successful')
conn.close()

