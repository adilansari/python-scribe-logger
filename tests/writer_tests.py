from scribe_logger.writer import ScribeWriter
from scribe_logger.connection import Connection
from collections import defaultdict
from unittest import TestCase
from mock import Mock
from json import dumps
from thrift.Thrift import TException
from scribe_logger.exceptions import ScribeLoggerError


class WriterTestCase(TestCase):

    HOST = 'test_host'
    PORT = 91464

    def setUp(self):
        self.mock_connection = Mock(spec=Connection)
        self.mock_connection.send = lambda self: True
        self.writer = ScribeWriter(self.HOST, self.PORT)
        self.writer.client = self.mock_connection

    def test_invalid_writes(self):
        self.assertRaises(TypeError, self.writer.write)
        self.assertRaises(ValueError, self.writer.write, ['message', defaultdict()])
        self.assertRaises(ValueError, self.writer.write, defaultdict())
        self.assertRaises(ValueError, self.writer.write, {'k': 'v'})
        self.assertRaises(ValueError, self.writer.write, 12345)

    def test_valid_writes(self):
        self.assertIsNone(self.writer.write('message'))
        self.assertIsNone(self.writer.write(['m1', 'm2']))
        self.assertIsNone(self.writer.write([]))
        self.assertIsNone(self.writer.write([dumps(defaultdict()), 'message']))
        self.assertIsNone(self.writer.write(dumps(defaultdict())))

    def test_failed_writes(self):
        self.mock_connection.send = lambda self: False
        self.writer.client = self.mock_connection
        with self.assertRaises(ScribeLoggerError):
            self.writer.write('message')

    def test_connection_error(self):
        self.writer = ScribeWriter(self.HOST, self.PORT)
        with self.assertRaises(TException):
            self.writer.write('message')
