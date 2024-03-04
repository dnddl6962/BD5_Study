def uploader(db_connector, pandas_df, table_name):

    with db_connector as connected:
        
        if connected.engine == 'postgresql':
            orm_conn = connected.orm_conn     ## postgres
        else:
            orm_conn = connected.conn           ## MYSQL
        
        pandas_df.to_sql(table_name, con=orm_conn, if_exists='replace', index=False)

    return('업로드 완료')