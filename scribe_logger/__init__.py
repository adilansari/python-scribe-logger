"""
Dependency check
"""
try:
    import scribe
    import thrift
except ImportError as e:
    raise ImportError('{}. {}'.format(e.message, "Run 'pip install -U -r requirements.txt'"))
