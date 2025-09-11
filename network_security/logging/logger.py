import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_dir=os.path.join(os.getcwd(),'Logs')
os.makedirs(LOG_FILE_dir,exist_ok=True)
LOG_FILE_PATH=os.path.join(LOG_FILE_dir,LOG_FILE_NAME)

logging.basicConfig(
    
    filename=LOG_FILE_PATH,
    format=" [ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



