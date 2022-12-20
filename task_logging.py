import logging
import time


def func():
    logging.debug('Debug msg')
    logging.info('Info msg')
    logging.error('Error msg')
    logging.warning('Warning msg')
    logging.critical('Crit msg')
    return None

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s-%(process)d-%(levelname)s-%(asctime)s-%(message)s', level=logging.INFO)
# logging.info('Admin logged in')
# time.sleep(3)
# logging.warning('This is a Warning')

# a = 5
# b = 0
# try:
#     c = a / b
# except ZeroDivisionError as e:
#     logging.info('**************************')
#     logging.error("Exception occurred", exc_info=True)
#     logging.info('--------------------------')
#     logging.exception("Exception occurred")

logger = logging.getLogger('Example_logger')
logger.warning('This is a warning')
logging.warning('This is a warning')

