import requests


class BurrowException(Exception):
    pass


class Request(object):
    """The base configuration class for each nested request.
    """
    requestlib = requests  # TODO: make switchable
    name = ''
    method = ''
    url = ''
    headers = {}
    payload = {}

    # Marks the behavior on a certain response status code with a class
    # If not specified, assumed as failure
    # also, not sure if this is to be specified here or in the config
    # please check test data to see what the currest pattern is
    http_200 = None
    http_400 = BurrowException

    @classmethod
    def data(cls):
        return cls.payload

    @classmethod
    def http_supported(cls):
        return cls.method.upper() in HTTP_METHODS

    @classmethod
    def response(cls, **kwargs):
        return getattr(cls.requestlib, cls.method(**kwargs))


class GETRequest(Request):
    """Currently not supported because need to implement url 'reverse' """
    method = 'get'


class POSTRequest(Request):
    method = 'post'

