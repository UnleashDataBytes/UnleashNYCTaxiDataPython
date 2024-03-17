import pandas as pd
import requests
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine, inspect

# Define the Schema
schema = {
    "vendorid": "str",
    "lpep_pickup_datetime": "str",
    "lpep_dropoff_datetime": "str",
    "store_and_fwd_flag": "str",
    "ratecodeid": "str",
    "pickup_longitude": "float",
    "pickup_latitude": "float",
    "dropoff_longitude": "float",
    "dropoff_latitude": "float",
    "passenger_count": "int",
    "trip_distance": "float",
    "fare_amount": "float",
    "extra": "float",
    "mta_tax": "float",
    "tip_amount": "float",
    "tolls_amount": "float",
    "imp_surcharge": "float",
    "total_amount": "float",
    "payment_type": "str",
    "trip_type": "str"
}

# Fetch data from API
api_url = "https://data.cityofnewyork.us/resource/hvrh-b6nb.json"
response = requests.get(api_url)
data = response.json()

# Convert data to DataFrame
df = pd.DataFrame(data, columns=schema.keys())

# Print DataFrame to verify data
print("DataFrame:")
print(df.head())

# Define Snowflake connection parameters
conn_params = {
    'account': 'account name', # Replace with your account name
    'user': 'user name', # Replace with your username
    'password': 'password',   # Replace with your password
    'warehouse': 'NYCTAXI',
    'database': 'NYCTAXIDATABASE',
    'schema': 'public'
}

table_name = 'trips'
engine = create_engine(URL(**conn_params))
inspector = inspect(engine)

df.to_sql(table_name, engine, schema=conn_params['schema'], if_exists='append', index=False)
print("Data inserted into Snowflake table successfully.")

engine.dispose()