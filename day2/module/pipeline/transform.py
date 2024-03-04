from datetime import datetime
import os
import pandas as pd

def create_path(temp_path, batch_data, table_name):     
    _y = batch_data[:4]
    _m = batch_data[4:6]
    _d = batch_data[6:]

    _path = os.path.join(temp_path, table_name, f'yyyy={_y}', f'mm={_m}', f'dd={_d}')

    return _path

def save_to_file(pandas_df, path, table_name):

    if len(pandas_df) > 0:

        # 경로 설정
        os.makedirs(path, mode=777)
        save_path = os.path.join(path, f'{table_name}.csv')
        # 파일로 저장
        pandas_df.to_csv(save_path)
        return True
    
    else:
        print('EMPTY FILE')
        return False

def transformer(temp_path, batch_date, pandas_df, table_name):

    path = create_path(temp_path, batch_date, table_name)

    response = save_to_file(pandas_df, path, table_name)

    return response, path