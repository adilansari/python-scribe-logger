"""Scribe Writer Class

This class handles writing to a scribe instance. The difference
between this class and logger is that this allows you to stream raw
data in your own format.

*Usage*
>>> from scribe_logger.writer import ScribeWriter
>>> writer = ScribeWriter('localhost', 1463, "category")
>>> writer.write("my message")
"""

from scribe_logger.connection import Connection
from scribe import scribe
from scribe_logger.exceptions import ScribeLoggerError


class ScribeWriter(object):

    """Default category to write to"""
    DEFAULT_CATEGORY = 'default'
    SILENT = False

    def __init__(self, host, port, category=DEFAULT_CATEGORY, silent=SILENT):
        self.category = category
        self.client = Connection(host, port)
        ScribeWriter.SILENT = silent

    def write(self, data):
        """
        Write data to scribe instance.
        arguments:
        data -- String or list of Strings to be written to Scribe
        """
        messages = self._generate_log_entries(data)

        try:
            self.client.init_connection()
        except Exception as e:
            self._raise(e.message)

        if not self.client.send(messages):
            self._raise('Write failed!')

    def _raise(self, message):
        if ScribeWriter.SILENT:
            return
        else:
            raise ScribeLoggerError(message)

    def _generate_log_entries(self, data):
        def __generate_log_entries(data):
            data = data if isinstance(data, list) else [data]
            messages = []
            for msg in data:
                if isinstance(msg, basestring):
                    messages.append(scribe.LogEntry(category=self.category, message=msg))
                else:
                    raise ValueError("Illegal argument to 'write'. Expected a string or list of strings")

            return messages

        return __generate_log_entries(data)
