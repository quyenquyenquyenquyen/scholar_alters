import logging
import os
from .config import LOGS_FOLDER

log_file = os.path.join(LOGS_FOLDER, "logs.log")
logging.basicConfig(
    force=True,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[logging.FileHandler(log_file)]
)