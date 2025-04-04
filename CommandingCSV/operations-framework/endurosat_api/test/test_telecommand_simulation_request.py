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
from endurosat_api.models.telecommand_simulation_request import TelecommandSimulationRequest  # noqa: E501
from endurosat_api.rest import ApiException

class TestTelecommandSimulationRequest(unittest.TestCase):
    """TelecommandSimulationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TelecommandSimulationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = endurosat_api.models.telecommand_simulation_request.TelecommandSimulationRequest()  # noqa: E501
        if include_optional :
            return TelecommandSimulationRequest(
                timestamp = 56, 
                uid = 56, 
                flags = 56, 
                command = endurosat_api.models.command_config.CommandConfig(
                    mac_interface_id = 56, 
                    target_address = 56, 
                    priority = 56, 
                    timeout = 56, 
                    command_bytes = '', )
            )
        else :
            return TelecommandSimulationRequest(
                timestamp = 56,
                uid = 56,
                flags = 56,
                command = endurosat_api.models.command_config.CommandConfig(
                    mac_interface_id = 56, 
                    target_address = 56, 
                    priority = 56, 
                    timeout = 56, 
                    command_bytes = '', ),
        )

    def testTelecommandSimulationRequest(self):
        """Test TelecommandSimulationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
