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

    def _is_scribe_ready(self):
        """Check to see if scribe is ready to be written to"""
        if self.transport.isOpen():
            return True

        self.lock.acquire()
        try:
            self.transport.open()
        except Exception:
            self.transport.close()
            raise
        finally:
            self.lock.release()

    def send(self, messages):
        """
        Sends the log stream to scribe
        arguments:
        messages -- list of LogEntry() objects
        """

        self._is_scribe_ready()
        self.lock.acquire()
        try:
            return (self.client.Log(messages=messages) == 0)
        except TException:
            self.transport.close()
            raise
        finally:
            self.lock.release()
