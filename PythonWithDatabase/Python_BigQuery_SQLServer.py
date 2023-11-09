import os 
import db_dtypes
import pyodbc
import pymssql
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from google.cloud import bigquery 

# declare all variables
v_key_path = '\\path\subpath\file.json' # this file holds both public, private key, service account details

# impersonate the account
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = v_key_path

# initiate the client that will be used to read data from bigquery tables
client = bigquery.Client.from_service_account_json(v_key_path)

# write your required sql query 
sourceSql = """select * from project.dataset.tablename limit 10"""

# execute the query 
query_job = client.query(sourceSql)

# retrieve the results into a rdd format
results = query_job.result()

# display the results 
print(type(results))

for row in results:
    print(row)

# load the data to a dataframe
df = results.to_dataframe()

# print the dataframe results
print(df.dtypes)
print(df)

# write data to SQL Server
## enter your server details
v_user = 'enter your username'
v_pwd = 'enter your password'

v_host = 'servername'
v_database = 'database name'
v_schema = 'dbo'
v_conn_str = f"mssql+pymssql://{v_user}:{v_pwd}@{v_host}/{v_database}"
print(v_conn_str)

v_tablename = 'tableName'
v_mode = 'append'
v_chunksize = 1000

engine = create_engine(v_conn_str, poolclass=NullPool)
sql_conn = engine.connect()

# write the data from dataframe to sql server
df.to_sql(name=v_tablename,con=sql_conn,schema=v_schema,index=False, if_exists=v_mode, chunksize = v_chunksize)

#close the connection
sql_conn.close()
print("written data from pandas to table ")






