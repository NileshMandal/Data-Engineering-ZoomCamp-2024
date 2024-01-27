#!/usr/bin/env python
# coding: utf-8


import argparse
import os
import pandas as pd
from sqlalchemy import create_engine
from time import time

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    url = params.url

    csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}'.format(
    user=user,
    password=password,
    host=host,
    port=port,
    db=db))

    df_iterator = pd.read_csv(csv_name, compression='gzip',low_memory=False, iterator=True, chunksize=100000)

    df = next(df_iterator)

#    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

#    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


    df.head(0).to_sql(name=table,con = engine,if_exists = 'replace')

    df.to_sql(name=table,con = engine,if_exists = 'append')

    while True:
        try:
            t_start = time()
            df = next(df_iterator)

 #           df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

#            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

            df.to_sql(name=table, con=engine, if_exists='append')
            t_end = time()

            print('Inserted another chunk..., time took:', (t_end - t_start))

        except StopIteration:
            print('Finished reading the CSV file.')
            break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest csv file to Postgres Table.')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table', help='table name of postgres')
    parser.add_argument('--url', help='url for the csv file')

    args = parser.parse_args()

    main(args)

