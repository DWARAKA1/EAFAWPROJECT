import sys
sys.path.append('src')

from src.common.logger import get_logger

def test_logging():
    logger = get_logger(__name__)
    logger.info("Test log message - INFO")
    logger.warning("Test log message - WARNING")
    logger.error("Test log message - ERROR")
    print("Logging test completed")

if __name__ == "__main__":
    test_logging()