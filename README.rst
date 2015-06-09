|Build Status| |Code Climate| |Coverage Status| |License| |Downloads|

Scribe logger
================

This package contains a low level interface for writing to Scribe, as
well as a higher level log handler which plays nicely with Python's
logging facilities.

    Supports Python 2.7

Installation
-----------------

``pip install scribe-logger``

Testing locally
--------------------

::

    git clone https://github.com/adilansari/python-scribe-logger.git
    cd python-scribe-logger
    pip install -U -r requirements.txt
    python runtests.py

Logger usage
-----------------

.. code:: python

    from scribe_logger.logger import ScribeLogHandler
    import logging

    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)

    scribe = ScribeLogHandler('localhost', 1464, category='test_category')
    scribe.setLevel(logging.DEBUG)
    my_logger.addHandler(scribe)

    my_logger.info('This is a test message')

``Logger raises exceptions``

Writer usage
-----------------

.. code:: python

    from scribe_logger.writer import ScribeWriter

    writer = ScribeWriter('localhost', 1464, 'test_category')
    try:
        writer.write('test_message_1')
        writer.write(['test_message_1', 'test_message_2', 'test_message_3'])
    except ScribeLoggerError:
        raise

Use **silent=True** To suppress exceptions:

.. code:: python

    writer = ScribeWriter('localhost', 1464, 'test_category', silent=True)
    writer.write('test_message_1')
    writer.write(['test_message_1', 'test_message_2', 'test_message_3'])

Contributors
-----------------

@adilansari @mwhooker @lenn0x

.. |Build Status| image:: https://travis-ci.org/adilansari/python-scribe-logger.svg?branch=master
   :target: https://travis-ci.org/adilansari/python-scribe-logger
.. |Code Climate| image:: https://codeclimate.com/github/adilansari/python-scribe-logger/badges/gpa.svg
   :target: https://codeclimate.com/github/adilansari/python-scribe-logger
.. |Coverage Status| image:: https://coveralls.io/repos/adilansari/python-scribe-logger/badge.svg?branch=master
   :target: https://coveralls.io/r/adilansari/python-scribe-logger?branch=master
.. |Supported Python versions| image:: https://pypip.in/py_versions/scribe_logger/badge.svg
   :target: https://pypi.python.org/pypi/scribe_logger/
.. |License| image:: https://img.shields.io/github/license/adilansari/python-scribe-logger.svg
   :target: https://github.com/adilansari/python-scribe-logger/blob/master/LICENSE.mkd
.. |Downloads| image:: https://img.shields.io/pypi/dm/scribe_logger.svg
   :target: https://pypi.python.org/pypi/scribe_logger/
