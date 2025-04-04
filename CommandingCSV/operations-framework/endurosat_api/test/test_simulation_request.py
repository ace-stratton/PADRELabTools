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
from endurosat_api.models.simulation_request import SimulationRequest  # noqa: E501
from endurosat_api.rest import ApiException

class TestSimulationRequest(unittest.TestCase):
    """SimulationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SimulationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = endurosat_api.models.simulation_request.SimulationRequest()  # noqa: E501
        if include_optional :
            return SimulationRequest(
                satellite_id = '', 
                telecommands = [
                    endurosat_api.models.telecommand_simulation_request.TelecommandSimulationRequest(
                        timestamp = 56, 
                        uid = 56, 
                        flags = 56, 
                        command = endurosat_api.models.command_config.CommandConfig(
                            mac_interface_id = 56, 
                            target_address = 56, 
                            priority = 56, 
                            timeout = 56, 
                            command_bytes = '', ), )
                    ], 
                simulation_config = endurosat_api.models.simulation_config.SimulationConfig(
                    sim_mode = 'ADCS', 
                    initial_mode = 'SAFE', 
                    number_of_orbits = 56, 
                    time_step = 56, 
                    max_integration_time_step = 56, 
                    start_with_tumbling = True, 
                    initial_rate = [
                        1.337
                        ], 
                    no_torques = True, 
                    no_disturb_torques = True, 
                    rw_imbalance_model = 'ADVANCED', 
                    stop_on_rw_saturation = True, 
                    include_sensor_views = True, 
                    include_est_ctrl_compatibility = True, 
                    nadir_mode_in_eclipse = True, 
                    mode_transition_threshold = 1.337, 
                    mode_transition_samples = 56, ), 
                orbit_config = endurosat_api.models.orbit_config.OrbitConfig(
                    start_time = [
                        56
                        ], 
                    tp = 56, 
                    sma = 56, 
                    eccentricity = 1.337, 
                    inclination = 1.337, 
                    aop = 1.337, 
                    raan = 1.337, 
                    ltan = 1.337, 
                    separation_angle = 1.337, 
                    altitude_difference = 1.337, 
                    position_error_rtn = [
                        56
                        ], )
            )
        else :
            return SimulationRequest(
                satellite_id = '',
                telecommands = [
                    endurosat_api.models.telecommand_simulation_request.TelecommandSimulationRequest(
                        timestamp = 56, 
                        uid = 56, 
                        flags = 56, 
                        command = endurosat_api.models.command_config.CommandConfig(
                            mac_interface_id = 56, 
                            target_address = 56, 
                            priority = 56, 
                            timeout = 56, 
                            command_bytes = '', ), )
                    ],
        )

    def testSimulationRequest(self):
        """Test SimulationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
