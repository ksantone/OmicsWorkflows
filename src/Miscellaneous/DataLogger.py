import logging

class DataLogger():

    def __init__(self):
        pass

    def log_error(self, error_msg):
        logging.error("log_file.txt", error_msg)

    def log_debug(self, debug_msg):
        logging.debug("log_file.txt", debug_msg)

    def log_warning(self, warning_msg):
        logging.debug("log_file.txt", warning_msg)