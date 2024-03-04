import pandas as pd
from db import postgresql_query, mysql_query

def extractor(db_connector, table_name, batch_date):
    with db_connector as connected:
        _query = connected.get_query(table_name, batch_date)
        print(_query)
        con = connected.conn
        df = pd.read_sql(_query, con)

        return df