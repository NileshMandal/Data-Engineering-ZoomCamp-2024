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

    if url.endswith('.gz'):
        os.system(f"wget {url} -O - | gzip -d > {csv_name}")
    else:
        os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iterator = pd.read_csv(csv_name, compression='gzip' if url.endswith('.gz') else None, low_memory=False, iterator=True, chunksize=100000)

    df = next(df_iterator)

    df.head(0).to_sql(name=table, con=engine, if_exists='replace', index=False)

    df.to_sql(name=table, con=engine, if_exists='append', index=False)

    while True:
        try:
            t_start = time()
            df = next(df_iterator)
            df.to_sql(name=table, con=engine, if_exists='append', index=False)
            t_end = time()

            print('Inserted another chunk..., time took:', (t_end - t_start))

        except StopIteration:
            print('Finished reading the CSV file.')
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest csv file to PostgreSQL Table.')
    parser.add_argument('--user', help='username for PostgreSQL')
    parser.add_argument('--password', help='password for PostgreSQL')
    parser.add_argument('--host', help='host for PostgreSQL')
    parser.add_argument('--port', help='port for PostgreSQL')
    parser.add_argument('--db', help='database name for PostgreSQL')
    parser.add_argument('--table', help='table name of PostgreSQL')
    parser.add_argument('--url', help='url for the csv file')

    args = parser.parse_args()
    main(args)
