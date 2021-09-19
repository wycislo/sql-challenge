# write python program to connect to postgres and load data to postgre database
#
# conda install psycopg2 - PostgresSQL database adapter for Python
#
#
#
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

departments_df = pd.read_csv('data/departments.csv')
dept_df = pd.read_csv('data/dept_emp.csv')
dept_manager_df = pd.read_csv('data/dept_manager.csv')
employees_df = pd.read_csv('data/employees.csv')
salaries_df = pd.read_csv('data/salaries.csv')
titles_df = pd.read_csv('data/titles.csv')


# # sqlachemy

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/company')

# # load df to database
departments_df.to_sql('departments',engine,index=False,if_exists='append')
print('departments')
dept_df.to_sql('dept_emp',engine,index=False,if_exists='append')
print('dept_emp')
dept_manager_df.to_sql('dept_manager',engine,index=False,if_exists='append')
print('dept_manager')
employees_df.to_sql('employees',engine,index=False,if_exists='append')
print('employees')
salaries_df.to_sql('salaries',engine,index=False,if_exists='append')
print('salaries')
titles_df.to_sql('titles',engine,index=False,if_exists='append')
print('titles')
dept_df.to_sql('dept_emp',engine,index=False,if_exists='append')
print('dept_emp')

