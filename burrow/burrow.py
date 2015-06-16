# -*- coding: utf-8 -*-

# Currently only post is supported. GET requires a way to handle urls
HTTP_METHODS = ('POST',)


def _make_request(requset, response=None):
    """This is the code that actually makes the request.

    Passing the response is optional as the top level requests are not expected
    to consume a previous response.
    This may change and at the moment the code may not be extensible to support
    this

    Cannot think of a situation where a caller should need to access this
    directly so it is marked private"""


def burrower(routes):
    """takes an map of Burrow Requests and follows the control flow
    """
    order = routes['order']

    for request in order:
        response = _make_request(request)
        nested_route = routes[request].get(response.status_code)

        if not nested_route:
            # handle_failure() to raise exception or call fail mode
            # or `continue`
            raise NotImplementedError

        # limited to one level deep for simplicity during the prototyping phase
        _make_request(nested_route, response)
