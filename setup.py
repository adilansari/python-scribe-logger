from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='scribe_logger',
    version='1.2',
    description='Scribe log writer and logging handler.',
    long_description=long_description,
    license='MIT',
    author='Chris Goffinet, Matthew Hooker, Adil Ansari',
    author_email='me@adilansari.com',
    maintainer='Adil Ansari',
    maintainer_email='me@adilansari.com',
    url='https://github.com/adilansari/python-scribe-logger',
    packages=['scribe_logger'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='scribe logging',
    install_requires=[
        'facebook-scribe==2.0',
        'thrift==0.9.2'
    ],
    extras_require={
        'test': ['nose==1.3.6', 'mock==1.0.1', 'coverage==3.7.1']
    }
)
