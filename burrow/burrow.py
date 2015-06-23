# -*- coding: utf-8 -*-
import requests

# Currently only post is supported. GET requires a way to handle urls
HTTP_METHODS = ('POST',)


def _get_config_attrs(request):
    """Hack to get config attrs which are class variables

    Cannot think of a situation where a caller should need to access this
    directly so it is marked private"""
    return {k: v for k, v in vars(request).items() if not k.startswith('__')}


def _sanitize_config_params(request):
    """this sanitizes the params passed to the requests method

    Q: should this be done after _get_config_attrs or before?
    """
    raise NotImplementedError


def _make_request(request, response=None):
    """This is the code that actually makes the request.

    Passing the response is optional as the top level requests are not expected
    to consume a previous response.
    This may change and at the moment the code may not be extensible to support
    this

    Cannot think of a situation where a caller should need to access this
    directly so it is marked private"""
    f = getattr(requests, request.method)

    if response:
        raise NotImplementedError

    # TODO: need to sanitize as well before this will actually work
    # one example is `fail_mode` blows up because requests doesn't know
    # what to do with it
    f(**_get_config_attrs(request))


def burrower(routes):
    """takes an map of Burrow Requests and follows the control flow
    """
    order = routes['order']

    for request in order:
        response = _make_request(request)
        nested_route = routes[request].get(response.status_code)

        if not nested_route:
            # TODO: handle_failure() to raise exception or call fail mode
            continue

        # limited to one level deep for simplicity during the prototyping phase
        _make_request(nested_route, response)
