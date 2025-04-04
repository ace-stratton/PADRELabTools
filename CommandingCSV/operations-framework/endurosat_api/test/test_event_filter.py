# coding: utf-8

"""
    EnduroSat SpaceOps REST API

    Documentation for EnduroSat SpaceOps REST API  # noqa: E501

    The version of the OpenAPI document: 0.34.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import endurosat_api
from endurosat_api.models.event_filter import EventFilter  # noqa: E501
from endurosat_api.rest import ApiException

class TestEventFilter(unittest.TestCase):
    """EventFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = endurosat_api.models.event_filter.EventFilter()  # noqa: E501
        if include_optional :
            return EventFilter(
                _property = '', 
                operator = '', 
                value = None
            )
        else :
            return EventFilter(
                _property = '',
                operator = '',
                value = None,
        )

    def testEventFilter(self):
        """Test EventFilter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
