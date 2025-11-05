import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    # Ensure file handler is attached only once
    log_file = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")
    if not any(isinstance(h, logging.FileHandler) and h.baseFilename == log_file for h in logger.handlers):
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
    return logger

# Self-test block
if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("LOGGER MODULE TEST: If you see this, logger.py is writing to the log file.")
    print("logger.py test executed. Check logs directory for output.")