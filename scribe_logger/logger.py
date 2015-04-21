"""Scribe Logger Class

This class handles overwriting logging to send to a scribe instance.

"""
from scribe_logger.writer import ScribeWriter
import logging
import logging.handlers


class ScribeLogHandler(logging.Handler, ScribeWriter):

    def __init__(self, host, port, category='default'):
        logging.Handler.__init__(self)
        ScribeWriter.__init__(self, host, port, category)

    def emit(self, record):
        record = self.format(record)
        try:
            self.write(record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
        finally:
            self.flush()

    def flush(self):
        pass
