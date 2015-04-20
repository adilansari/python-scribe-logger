from scribe_logger.connection import Connection
from unittest import TestCase
from mock import Mock
from thrift.Thrift import TException


class ConnectionTestCase(TestCase):

    HOST = 'localhost'
    PORT = 1464

    def test_valid_connection(self):
        mock_connection = Mock(spec=Connection)
        mock_connection.is_ready = lambda: True
        self.assertTrue(mock_connection.is_ready)

    def test_invalid_connection(self):
        connection = Connection(self.HOST, self.PORT)

        try:
            connection._init_connection()
        except TException:
            self.assertFalse(connection.is_ready)
        else:
            self.assertTrue(connection.is_ready)
        finally:
            connection.close()
