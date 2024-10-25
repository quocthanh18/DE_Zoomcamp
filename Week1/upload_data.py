import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
def main():
    user= os.getenv('POSTGRES_USER')
    password= os.getenv('POSTGRES_PASSWORD')
    host= os.getenv('host')
    port= os.getenv('port')
    database= os.getenv('POSTGRES_DB')
    table = os.getenv('table')
    url = os.getenv('url')
    parquet = 'output.parquet'
    os.system(f'wget {url} -O {parquet}')
    data = pd.read_parquet(f'{parquet}')
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
    engine.connect()
    data.to_sql(f'{table}', engine, if_exists='replace', index=False)


if __name__ == '__main__':
    main()
