"""
Dependency check
"""
try:
    import scribe
    import thrift
except ImportError, e:
    raise ImportError('{}. {}'.format(e.message, "Run 'pip install -U -r requirements.txt'"))
