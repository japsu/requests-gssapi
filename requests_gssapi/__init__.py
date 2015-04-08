"""
requests Kerberos/GSSAPI authentication library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings. This library
adds optional Kerberos/GSSAPI authentication support and supports mutual
authentication. Basic GET usage:

    >>> import requests
    >>> from requests_gssapi import HTTPGSSAPIAuth
    >>> r = requests.get("http://example.org", auth=HTTPGSSAPIAuth())

The entire `requests.api` should be supported.
"""
import logging

from .implementation import HTTPGSSAPIAuth, REQUIRED, OPTIONAL, DISABLED
from .exceptions import MutualAuthenticationError

logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = ('HTTPGSSAPIAuth', 'MutualAuthenticationError', 'REQUIRED',
           'OPTIONAL', 'DISABLED')
__version__ = '0.6.1'
