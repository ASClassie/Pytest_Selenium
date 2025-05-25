import logging
import os
from datetime import datetime
import platform
import sys


class TestLogger:
    """
    Custom logger class for test automation framework.
    Creates logs in D:\Pytest_Selenium\test-results\logs directory.
    """

    def __init__(self, log_level=logging.DEBUG):
        """
        Initialize logger with specified log level

        Args:
            log_level: Logging level (default: logging.INFO)
        """
        # Root directory for logs
        if platform.system() == 'Windows':
            self.root_dir = r"D:\Pytest_Selenium"
        else:
            # For non-Windows systems, use current directory
            self.root_dir = os.getcwd()

        # Create logs directory structure
        self.logs_dir = os.path.join(self.root_dir, "test-results", "logs")
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create timestamp for log filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file = os.path.join(self.logs_dir, f"test_log_{timestamp}.log")

        # Configure logger
        self.logger = logging.getLogger("test_framework")
        self.logger.setLevel(log_level)
        self.logger.handlers = []  # Clear existing handlers to avoid duplicates

        # Create file handler
        file_handler = logging.FileHandler(self.log_file)

        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Set formatter to handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # Initial log message
        self.info(f"Logger initialized. Log file: {self.log_file}")

    def info(self, message):
        """Log info level message"""
        self.logger.info(message)

    def debug(self, message):
        """Log debug level message"""
        self.logger.debug(message)

    def warning(self, message):
        """Log warning level message"""
        self.logger.warning(message)

    def error(self, message):
        """Log error level message"""
        self.logger.error(message)

    def critical(self, message):
        """Log critical level message"""
        self.logger.critical(message)

    def get_logger(self):
        """Return the logger instance"""
        return self.logger

    def get_log_file_path(self):
        """Return the current log file path"""
        return self.log_file


# Example usage
if __name__ == "__main__":
    # Create logger instance
    test_logger = TestLogger()

    # Log sample messages
    test_logger.info("This is an information message")
    test_logger.debug("This is a debug message")
    test_logger.warning("This is a warning message")
    test_logger.error("This is an error message")
    test_logger.critical("This is a critical message")

    print(f"Log file created at: {test_logger.get_log_file_path()}")