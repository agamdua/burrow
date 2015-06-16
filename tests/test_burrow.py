#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_burrow
----------------------------------

Tests for `burrow` module.
"""

import unittest

from burrow.burrow import burrower
from burrow.request import POSTRequest


class TestBurrow(unittest.TestCase):

    def setUp(self):
        class FirstRequest(POSTRequest):
            url = 'url'
            name = 'first_request'
            status_failure = lambda x: x != 200
            fail_modes = (status_failure,)

        class SecondRequest(POSTRequest):
            name = 'second_request'
            url = 'url2'

        class ThirdRequest(POSTRequest):
            name = 'third_request'
            url = 'url2'

        self.burrows = {
            'order': (FirstRequest, SecondRequest,),
            FirstRequest: {
                200: SecondRequest,
                400: ThirdRequest
            },
            SecondRequest: {
                200: ThirdRequest
            }
        }

    @unittest.expectedFailure
    def test_burrower(self):
        self.assertEqual(
            burrower(self.burrows), 'third_request'
        )

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
