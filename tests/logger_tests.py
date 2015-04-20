from scribe_logger.logger import ScribeLogHandler
from scribe_logger.connection import Connection
from unittest import TestCase
from mock import Mock
import logging


class LoggerTestCase(TestCase):

    HOST = 'localhost'
    PORT = 1464

    def setUp(self):
        self.mock_connection = Mock(spec=Connection)
        self.mock_connection.send.return_value = True

    def test_valid_logging(self):
        test_logger = logging.getLogger('test_valid_logging')
        test_logger.setLevel(logging.WARNING)
        mock_handler = ScribeLogHandler(self.HOST, self.PORT)
        mock_handler.client = self.mock_connection
        mock_handler.setLevel(logging.DEBUG)
        test_logger.addHandler(mock_handler)

        self.assertIsNone(test_logger.debug('message'))
        self.assertIsNone(test_logger.warning('message'))

    def test_invalid_logging(self):
        """
        Not passing valid extra parameter to
        """
        test_logger = logging.getLogger('test_invalid_logging')
        test_logger.setLevel(logging.WARNING)
        formatter = logging.Formatter('%(bad_arg)s - %(levelname)s - %(message)s')
        mock_handler = ScribeLogHandler(self.HOST, self.PORT)
        mock_handler.client = self.mock_connection
        mock_handler.setLevel(logging.DEBUG)
        mock_handler.setFormatter(formatter)
        test_logger.addHandler(mock_handler)

        self.assertIsNone(test_logger.debug('message'))
        self.assertIsNone(test_logger.warning('message', extra={'bad_arg': 'fail'}))

        with self.assertRaises(KeyError):
            test_logger.warning('message')

        with self.assertRaises(KeyError):
            test_logger.warning('message', extra={'k': 'v'})
