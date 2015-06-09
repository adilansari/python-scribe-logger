from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
import threading
from scribe import scribe
from thrift.Thrift import TException


class Connection(object):

    def __init__(self, host, port):
        self._configure_scribe(host, port)
        self.lock = threading.RLock()

    def _configure_scribe(self, host, port):
        self.socket = TSocket.TSocket(host=host, port=port)
        self.socket.setTimeout(1000)
        self.transport = TTransport.TFramedTransport(self.socket)
        self.protocol = TBinaryProtocol.TBinaryProtocolAccelerated(
            trans=self.transport,
            strictRead=False,
            strictWrite=False)
        self.client = scribe.Client(iprot=self.protocol, oprot=self.protocol)

    @property
    def is_ready(self):
        """
        Wrapper around _init_connection() bypassing Exception
        """
        return self.transport.isOpen()

    def close(self):
        """
        Close connection
        """
        if self.is_ready:
            self.transport.close()

    def init_connection(self):
        """Check to see if scribe is ready to be written to"""
        if self.is_ready:
            return

        def _init_connection(self):

            self.lock.acquire()
            try:
                self.transport.open()
            except Exception:
                self.close()
                raise
            finally:
                self.lock.release()

        _init_connection(self)

    def send(self, messages):
        """
        Sends the log stream to scribe
        arguments:
        messages -- list of LogEntry() objects
        """

        if not self.is_ready:
            return False

        self.lock.acquire()
        try:
            return (self.client.Log(messages=messages) == 0)
        except Exception:
            self.close()
            raise
        finally:
            self.lock.release()
