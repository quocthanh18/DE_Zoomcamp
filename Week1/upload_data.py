import argparse
import pandas as pd
from sqlalchemy import create_engine
import os
def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    database=params.database
    table=params.table
    url = params.url
    parquet = 'output.parquet'
    os.system(f'wget {url} -O {parquet}')
    data = pd.read_parquet(f'{parquet}')
    data.describe()


    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
    engine.connect()

    data.to_sql(f'{table}', engine, if_exists='replace', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--user')
    parser.add_argument('--password')
    parser.add_argument('--host')
    parser.add_argument('--port')
    parser.add_argument('--database')
    parser.add_argument('--table')
    parser.add_argument('--url')
    args = parser.parse_args()
    main(args)
