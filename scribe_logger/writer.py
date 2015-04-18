"""Scribe Writer Class

This class handles writing to a scribe instance. The difference
between this class and logger is that this allows you to stream raw
data in your own format.

*Usage*
>>> from scribe_logger.writer import ScribeWriter
>>> writer = ScribeWriter('localhost', 1463, "category")
>>> writer.write("another_category", "my message")

"""
from scribe import scribe
from thrift import Thrift
import threading
from scribe_logger import connection


class ScribeWriter(object):

    #: Default category to write to
    default_category = 'default'

    def __init__(self, host, port, category=default_category):
        self.category = category
        self.client = connection(host, port)
        self.lock = threading.RLock()

    def write(self, data):
        """Write data to scribe instance"""
        # data can be just a message or a list of messages

        if not self.client.is_ready():
            # raise ScribeNotReady
            return

        # this can be removed
        if not isinstance(data, list):
            data = [data]

        # find a better way to do this
        messages = self._generate_log_entries(data)

        self.client.send(messages)

    def _generate_log_entries(self, data):
        messages = []

        # this generate_log_entries()
        for msg in data:
            try:
                # this doesn't have to be a dict of course, find something better
                entry = scribe.LogEntry(category=self.category, message=msg)
            except Exception, e:
                entry = scribe.LogEntry(dict(category=self.category, message=msg))

            messages.append(entry)

            return messages
