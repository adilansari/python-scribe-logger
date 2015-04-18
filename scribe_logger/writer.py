"""Scribe Writer Class

This class handles writing to a scribe instance. The difference
between this class and logger is that this allows you to stream raw
data in your own format.

*Usage*
>>> from scribe_logger.writer import ScribeWriter
>>> writer = ScribeWriter('localhost', 1463, "category")
>>> writer.write("my message")
"""

from scribe import scribe
from connection import Connection


class ScribeWriter(object):

    """Default category to write to"""
    DEFAULT_CATEGORY = 'default'

    def __init__(self, host, port, category=DEFAULT_CATEGORY):
        self.category = category
        self.client = Connection(host, port)

    def write(self, data):
        """Write data to scribe instance

        arguments:
        data -- String or list of Strings to be written to Scribe
        """

        if not self.client.is_ready:
            raise Exception('client not ready')

        messages = self._generate_log_entries(data)
        self.client.send(messages)

    def _generate_log_entries(self, data):
        def __generate_log_entries(data):
            data = data if isinstance(data, list) else [data]
            messages = []
            for msg in data:
                if isinstance(msg, basestring):
                    messages.append(scribe.LogEntry(category=self.category, message=msg))
                else:
                    raise Exception('string or list of strings')

            return messages

        return __generate_log_entries(data)
