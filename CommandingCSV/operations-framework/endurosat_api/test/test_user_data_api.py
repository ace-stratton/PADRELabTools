# coding: utf-8

"""
    EnduroSat SpaceOps REST API

    Documentation for EnduroSat SpaceOps REST API  # noqa: E501

    The version of the OpenAPI document: 0.34.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import endurosat_api
from endurosat_api.api.user_data_api import UserDataApi  # noqa: E501
from endurosat_api.rest import ApiException


class TestUserDataApi(unittest.TestCase):
    """UserDataApi unit test stubs"""

    def setUp(self):
        self.api = endurosat_api.api.user_data_api.UserDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_user_data_with_key(self):
        """Test case for delete_user_data_with_key

        Delete User Data  # noqa: E501
        """
        pass

    def test_edit_user_data_with_key(self):
        """Test case for edit_user_data_with_key

        Edit User Data  # noqa: E501
        """
        pass

    def test_get_user_data_by_key(self):
        """Test case for get_user_data_by_key

        Get User Data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
