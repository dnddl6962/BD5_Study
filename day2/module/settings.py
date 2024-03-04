import os
import dotenv

# .env 경로 찾기
env_path = dotenv.find_dotenv()

# .env 파일 load
dotenv.load_dotenv(env_path)

TEMP_PATH = "../../Temp_storage"

DB_LIST = ['POSTGRES', 'MYSQL']

DB_SETTINGS = {
    "POSTGRES" : {
        'engine' : os.environ.get('POSTGRES_ENGINE'),
        'host' : os.environ.get('POSTGRES_HOST'),
        'dbname' : os.environ.get('POSTGRES_DB_1'),
        'user' : os.environ.get('POSTGRES_USER'),
        'password' : os.environ.get('POSTGRES_PASSWORD'),
        'port' : os.environ.get('POSTGRES_PORT')

    },
    "KDT" : {
        'engine' : os.environ.get('POSTGRES_ENGINE'),
        'host' : os.environ.get('POSTGRES_HOST'),
        'dbname' : os.environ.get('POSTGRES_DB_2'),
        'user' : os.environ.get('POSTGRES_USER'),
        'password' : os.environ.get('POSTGRES_PASSWARD'),
        'port' : os.environ.get('POSTGRES_PORT')
    },
    "MYSQL" : {
        'engine' : os.environ.get('MYSQL_ENGINE'),
        'host' : os.environ.get('MYSQL_HOST'),
        'dbname' : os.environ.get('MYSQL_DB_1'),
        'user' : os.environ.get('MYSQL_USER'),
        'password' : os.environ.get('MYSQL_PASSWARD'),
        'port' : os.environ.get('MYSQL_PORT')
    }
}
