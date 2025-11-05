import sys
try:
    from src.common.logger import get_logger
except ModuleNotFoundError:
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from logger import get_logger

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        logger = get_logger(__name__)
        self.error_message = self.get_detailed_error_message(message, error_detail)
        logger.error(self.error_message)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        return self.error_message

# Self-test block
if __name__ == "__main__":
    try:
        raise CustomException("CUSTOM_EXCEPTION MODULE TEST", Exception("Test error detail"))
    except CustomException as ce:
        print(f"custom_exception.py test executed: {ce}")
        print("Check logs directory for output.")
