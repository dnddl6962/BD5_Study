import shutil, os
from settings import TEMP_PATH

def remover(TEMP_PATH):
    
    shutil.rmtree(TEMP_PATH)

    os.makedirs(TEMP_PATH)