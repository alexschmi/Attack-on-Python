#Task 05: Logging

import logging


def init_log(file_name, file_mode, level, log_format, date_format):
    # Set the logging level
    logging.basicConfig(level=level)

    # Create a custom log file
    logging.basicConfig(filename=file_name, filemode=file_mode)

    # Set the logging format
    formatter = logging.Formatter(log_format, datefmt=date_format)

    # Add the formatter to the handler
    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger = logging.getLogger()
    logger.addHandler(handler)

    try:
        # Your task goes here
        raise Exception("This is a test exception")

    except Exception as e:
        # Log the error message
        logging.error(e)

    finally:
        # Close the log file
        logging.shutdown()


# Test the function
init_log("log.txt", "w", logging.ERROR, "%(asctime)s - %(levelname)s - %(message)s", "%m/%d/%Y %I:%M:%S %p")
