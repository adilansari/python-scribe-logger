from scribe_logger.logger import ScribeLogHandler
import logging

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

scribe = ScribeLogHandler('localhost', 1464, category='test_category')
scribe.setLevel(logging.DEBUG)
my_logger.addHandler(scribe)

my_logger.info('This is a test message')
