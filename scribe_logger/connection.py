from scribe import scribe
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol
from thrift import Thrift
import threading


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
        return self._is_scribe_ready()

    def _is_scribe_ready(self):
        """Check to see if scribe is ready to be written to"""
        if self.transport.isOpen():
            return True

        self.lock.acquire()
        try:
            self.transport.open()
            return True
        except Thrift.TException, tx:
            self.transport.close()
        except Exception, e:
            #raise ConnecionError
            self.transport.close()
        finally:
            self.lock.release()
        return False

    def send(self, messages):
        # move it to connection - send(messages)
        # find individual exceptions
        self.lock.acquire()
        try:
            self.client.Log(messages=messages)
        except Thrift.TException, tx:
            self.transport.close()
        except Exception, e:
            self.transport.close()
        finally:
            self.lock.release()
