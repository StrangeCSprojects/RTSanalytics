from logging_config_example import setup_logging
import logging
setup_logging()
# Retrieve the logger instance configured in the logging_config.py
logger = logging.getLogger(__name__)

def do_something():
    logger.info("Function do_something is starting")
    # Add some more detailed debug information
    logger.debug("Detailed debug information goes here")
    # Pretend to do some work
    try:
        # Potentially problematic code
        result = 10 / 0
    except ZeroDivisionError:
        logger.error("Tried to divide by zero", exc_info=True)
    else:
        logger.info("Result: %s", result)

    logger.info("Function do_something is ending")

if __name__ == "__main__":
    # Normally you'd call setup_logging in your main entry script
    # from logging_config import setup_logging
    # setup_logging()

    do_something()



