from db.connector import DBconnector
from settings import DB_SETTINGS, TEMP_PATH, DB_LIST
from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.loader import uploader
from datetime import datetime
from pipeline.remove import remover
from db import postgresql_query, mysql_query



def main(batch_date):

    for database in DB_LIST:

        if database == 'POSTGRES':
            table_list = list(postgresql_query.queries.keys())
        else:
            table_list = list(mysql_query.queries.keys())

        for table_name in table_list:
            print(table_name)
            # db_connector = DBconnector(**DB_SETTINGS['POSTGRES'])
            db_connector = DBconnector(**DB_SETTINGS[database])

            pandas_df = extractor(db_connector, table_name, batch_date)
            print(len(pandas_df))

            if len(pandas_df):
                
                response, path = transformer(TEMP_PATH, batch_date, pandas_df, table_name)

        #         uploader(db_connector, pandas_df, table_name)
                
        # remover(TEMP_PATH)