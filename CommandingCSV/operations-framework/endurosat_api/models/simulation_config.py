# coding: utf-8

"""
    EnduroSat SpaceOps REST API

    Documentation for EnduroSat SpaceOps REST API  # noqa: E501

    The version of the OpenAPI document: 0.34.7
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from endurosat_api.configuration import Configuration


class SimulationConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sim_mode': 'str',
        'initial_mode': 'str',
        'number_of_orbits': 'int',
        'time_step': 'int',
        'max_integration_time_step': 'int',
        'start_with_tumbling': 'bool',
        'initial_rate': 'list[float]',
        'no_torques': 'bool',
        'no_disturb_torques': 'bool',
        'rw_imbalance_model': 'str',
        'stop_on_rw_saturation': 'bool',
        'include_sensor_views': 'bool',
        'include_est_ctrl_compatibility': 'bool',
        'nadir_mode_in_eclipse': 'bool',
        'mode_transition_threshold': 'float',
        'mode_transition_samples': 'int'
    }

    attribute_map = {
        'sim_mode': 'simMode',
        'initial_mode': 'initialMode',
        'number_of_orbits': 'numberOfOrbits',
        'time_step': 'timeStep',
        'max_integration_time_step': 'maxIntegrationTimeStep',
        'start_with_tumbling': 'startWithTumbling',
        'initial_rate': 'initialRate',
        'no_torques': 'noTorques',
        'no_disturb_torques': 'noDisturbTorques',
        'rw_imbalance_model': 'rwImbalanceModel',
        'stop_on_rw_saturation': 'stopOnRwSaturation',
        'include_sensor_views': 'includeSensorViews',
        'include_est_ctrl_compatibility': 'includeEstCtrlCompatibility',
        'nadir_mode_in_eclipse': 'nadirModeInEclipse',
        'mode_transition_threshold': 'modeTransitionThreshold',
        'mode_transition_samples': 'modeTransitionSamples'
    }

    def __init__(self, sim_mode=None, initial_mode=None, number_of_orbits=None, time_step=None, max_integration_time_step=None, start_with_tumbling=None, initial_rate=None, no_torques=None, no_disturb_torques=None, rw_imbalance_model=None, stop_on_rw_saturation=None, include_sensor_views=None, include_est_ctrl_compatibility=None, nadir_mode_in_eclipse=None, mode_transition_threshold=None, mode_transition_samples=None, local_vars_configuration=None):  # noqa: E501
        """SimulationConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._sim_mode = None
        self._initial_mode = None
        self._number_of_orbits = None
        self._time_step = None
        self._max_integration_time_step = None
        self._start_with_tumbling = None
        self._initial_rate = None
        self._no_torques = None
        self._no_disturb_torques = None
        self._rw_imbalance_model = None
        self._stop_on_rw_saturation = None
        self._include_sensor_views = None
        self._include_est_ctrl_compatibility = None
        self._nadir_mode_in_eclipse = None
        self._mode_transition_threshold = None
        self._mode_transition_samples = None
        self.discriminator = None

        self.sim_mode = sim_mode
        if initial_mode is not None:
            self.initial_mode = initial_mode
        if number_of_orbits is not None:
            self.number_of_orbits = number_of_orbits
        if time_step is not None:
            self.time_step = time_step
        if max_integration_time_step is not None:
            self.max_integration_time_step = max_integration_time_step
        if start_with_tumbling is not None:
            self.start_with_tumbling = start_with_tumbling
        if initial_rate is not None:
            self.initial_rate = initial_rate
        if no_torques is not None:
            self.no_torques = no_torques
        if no_disturb_torques is not None:
            self.no_disturb_torques = no_disturb_torques
        if rw_imbalance_model is not None:
            self.rw_imbalance_model = rw_imbalance_model
        if stop_on_rw_saturation is not None:
            self.stop_on_rw_saturation = stop_on_rw_saturation
        if include_sensor_views is not None:
            self.include_sensor_views = include_sensor_views
        if include_est_ctrl_compatibility is not None:
            self.include_est_ctrl_compatibility = include_est_ctrl_compatibility
        if nadir_mode_in_eclipse is not None:
            self.nadir_mode_in_eclipse = nadir_mode_in_eclipse
        if mode_transition_threshold is not None:
            self.mode_transition_threshold = mode_transition_threshold
        if mode_transition_samples is not None:
            self.mode_transition_samples = mode_transition_samples

    @property
    def sim_mode(self):
        """Gets the sim_mode of this SimulationConfig.  # noqa: E501

        1: ADCS, 2: STMA] (adcs only, OBC state machine)  # noqa: E501

        :return: The sim_mode of this SimulationConfig.  # noqa: E501
        :rtype: str
        """
        return self._sim_mode

    @sim_mode.setter
    def sim_mode(self, sim_mode):
        """Sets the sim_mode of this SimulationConfig.

        1: ADCS, 2: STMA] (adcs only, OBC state machine)  # noqa: E501

        :param sim_mode: The sim_mode of this SimulationConfig.  # noqa: E501
        :type sim_mode: str
        """
        if self.local_vars_configuration.client_side_validation and sim_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `sim_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["ADCS", "STMA"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sim_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sim_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(sim_mode, allowed_values)
            )

        self._sim_mode = sim_mode

    @property
    def initial_mode(self):
        """Gets the initial_mode of this SimulationConfig.  # noqa: E501

        Initial operational mode, can only be 'safe' or 'idle'. Only relevant for simmode 2.  # noqa: E501

        :return: The initial_mode of this SimulationConfig.  # noqa: E501
        :rtype: str
        """
        return self._initial_mode

    @initial_mode.setter
    def initial_mode(self, initial_mode):
        """Sets the initial_mode of this SimulationConfig.

        Initial operational mode, can only be 'safe' or 'idle'. Only relevant for simmode 2.  # noqa: E501

        :param initial_mode: The initial_mode of this SimulationConfig.  # noqa: E501
        :type initial_mode: str
        """
        allowed_values = ["SAFE", "IDLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and initial_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `initial_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(initial_mode, allowed_values)
            )

        self._initial_mode = initial_mode

    @property
    def number_of_orbits(self):
        """Gets the number_of_orbits of this SimulationConfig.  # noqa: E501

        Maximum number of orbits, should be bigger or equal to the commanded time of the operational modes in OBC yaml [if not only adcs sim]  # noqa: E501

        :return: The number_of_orbits of this SimulationConfig.  # noqa: E501
        :rtype: int
        """
        return self._number_of_orbits

    @number_of_orbits.setter
    def number_of_orbits(self, number_of_orbits):
        """Sets the number_of_orbits of this SimulationConfig.

        Maximum number of orbits, should be bigger or equal to the commanded time of the operational modes in OBC yaml [if not only adcs sim]  # noqa: E501

        :param number_of_orbits: The number_of_orbits of this SimulationConfig.  # noqa: E501
        :type number_of_orbits: int
        """

        self._number_of_orbits = number_of_orbits

    @property
    def time_step(self):
        """Gets the time_step of this SimulationConfig.  # noqa: E501

        [s] subsystems loop period  # noqa: E501

        :return: The time_step of this SimulationConfig.  # noqa: E501
        :rtype: int
        """
        return self._time_step

    @time_step.setter
    def time_step(self, time_step):
        """Sets the time_step of this SimulationConfig.

        [s] subsystems loop period  # noqa: E501

        :param time_step: The time_step of this SimulationConfig.  # noqa: E501
        :type time_step: int
        """

        self._time_step = time_step

    @property
    def max_integration_time_step(self):
        """Gets the max_integration_time_step of this SimulationConfig.  # noqa: E501

        [s] maximum integration timestep  # noqa: E501

        :return: The max_integration_time_step of this SimulationConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_integration_time_step

    @max_integration_time_step.setter
    def max_integration_time_step(self, max_integration_time_step):
        """Sets the max_integration_time_step of this SimulationConfig.

        [s] maximum integration timestep  # noqa: E501

        :param max_integration_time_step: The max_integration_time_step of this SimulationConfig.  # noqa: E501
        :type max_integration_time_step: int
        """

        self._max_integration_time_step = max_integration_time_step

    @property
    def start_with_tumbling(self):
        """Gets the start_with_tumbling of this SimulationConfig.  # noqa: E501

        if True, no torques will be acting on the satellite (this setting is mainly for verification tests)  # noqa: E501

        :return: The start_with_tumbling of this SimulationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._start_with_tumbling

    @start_with_tumbling.setter
    def start_with_tumbling(self, start_with_tumbling):
        """Sets the start_with_tumbling of this SimulationConfig.

        if True, no torques will be acting on the satellite (this setting is mainly for verification tests)  # noqa: E501

        :param start_with_tumbling: The start_with_tumbling of this SimulationConfig.  # noqa: E501
        :type start_with_tumbling: bool
        """

        self._start_with_tumbling = start_with_tumbling

    @property
    def initial_rate(self):
        """Gets the initial_rate of this SimulationConfig.  # noqa: E501

        [deg/s] Initial rate in the body frame wrt ECI if starting with tumbling if startWithTumbling set to true.  # noqa: E501

        :return: The initial_rate of this SimulationConfig.  # noqa: E501
        :rtype: list[float]
        """
        return self._initial_rate

    @initial_rate.setter
    def initial_rate(self, initial_rate):
        """Sets the initial_rate of this SimulationConfig.

        [deg/s] Initial rate in the body frame wrt ECI if starting with tumbling if startWithTumbling set to true.  # noqa: E501

        :param initial_rate: The initial_rate of this SimulationConfig.  # noqa: E501
        :type initial_rate: list[float]
        """

        self._initial_rate = initial_rate

    @property
    def no_torques(self):
        """Gets the no_torques of this SimulationConfig.  # noqa: E501

        If true, no torques will be acting on the satellite  # noqa: E501

        :return: The no_torques of this SimulationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._no_torques

    @no_torques.setter
    def no_torques(self, no_torques):
        """Sets the no_torques of this SimulationConfig.

        If true, no torques will be acting on the satellite  # noqa: E501

        :param no_torques: The no_torques of this SimulationConfig.  # noqa: E501
        :type no_torques: bool
        """

        self._no_torques = no_torques

    @property
    def no_disturb_torques(self):
        """Gets the no_disturb_torques of this SimulationConfig.  # noqa: E501

        If true, there will be no disturbance torques simulated  # noqa: E501

        :return: The no_disturb_torques of this SimulationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._no_disturb_torques

    @no_disturb_torques.setter
    def no_disturb_torques(self, no_disturb_torques):
        """Sets the no_disturb_torques of this SimulationConfig.

        If true, there will be no disturbance torques simulated  # noqa: E501

        :param no_disturb_torques: The no_disturb_torques of this SimulationConfig.  # noqa: E501
        :type no_disturb_torques: bool
        """

        self._no_disturb_torques = no_disturb_torques

    @property
    def rw_imbalance_model(self):
        """Gets the rw_imbalance_model of this SimulationConfig.  # noqa: E501

        Reaction wheel imbalance model ['ADVANCED', 'SIMPLE', 'NOT']  # noqa: E501

        :return: The rw_imbalance_model of this SimulationConfig.  # noqa: E501
        :rtype: str
        """
        return self._rw_imbalance_model

    @rw_imbalance_model.setter
    def rw_imbalance_model(self, rw_imbalance_model):
        """Sets the rw_imbalance_model of this SimulationConfig.

        Reaction wheel imbalance model ['ADVANCED', 'SIMPLE', 'NOT']  # noqa: E501

        :param rw_imbalance_model: The rw_imbalance_model of this SimulationConfig.  # noqa: E501
        :type rw_imbalance_model: str
        """
        allowed_values = ["ADVANCED", "SIMPLE", "NOT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rw_imbalance_model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rw_imbalance_model` ({0}), must be one of {1}"  # noqa: E501
                .format(rw_imbalance_model, allowed_values)
            )

        self._rw_imbalance_model = rw_imbalance_model

    @property
    def stop_on_rw_saturation(self):
        """Gets the stop_on_rw_saturation of this SimulationConfig.  # noqa: E501

        End the simulation if RWs are saturated; else, continue  # noqa: E501

        :return: The stop_on_rw_saturation of this SimulationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._stop_on_rw_saturation

    @stop_on_rw_saturation.setter
    def stop_on_rw_saturation(self, stop_on_rw_saturation):
        """Sets the stop_on_rw_saturation of this SimulationConfig.

        End the simulation if RWs are saturated; else, continue  # noqa: E501

        :param stop_on_rw_saturation: The stop_on_rw_saturation of this SimulationConfig.  # noqa: E501
        :type stop_on_rw_saturation: bool
        """

        self._stop_on_rw_saturation = stop_on_rw_saturation

    @property
    def include_sensor_views(self):
        """Gets the include_sensor_views of this SimulationConfig.  # noqa: E501

        If True, the orientation of the sensors in the satellite will matter wrt sun earth blocking  # noqa: E501

        :return: The include_sensor_views of this SimulationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._include_sensor_views

    @include_sensor_views.setter
    def include_sensor_views(self, include_sensor_views):
        """Sets the include_sensor_views of this SimulationConfig.

        If True, the orientation of the sensors in the satellite will matter wrt sun earth blocking  # noqa: E501

        :param include_sensor_views: The include_sensor_views of this SimulationConfig.  # noqa: E501
        :type include_sensor_views: bool
        """

        self._include_sensor_views = include_sensor_views

    @property
    def include_est_ctrl_compatibility(self):
        """Gets the include_est_ctrl_compatibility of this SimulationConfig.  # noqa: E501

        If True, the Opsim will check the compatibility between control and estimation modes and transitions. if false, everything is allowed  # noqa: E501

        :return: The include_est_ctrl_compatibility of this SimulationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._include_est_ctrl_compatibility

    @include_est_ctrl_compatibility.setter
    def include_est_ctrl_compatibility(self, include_est_ctrl_compatibility):
        """Sets the include_est_ctrl_compatibility of this SimulationConfig.

        If True, the Opsim will check the compatibility between control and estimation modes and transitions. if false, everything is allowed  # noqa: E501

        :param include_est_ctrl_compatibility: The include_est_ctrl_compatibility of this SimulationConfig.  # noqa: E501
        :type include_est_ctrl_compatibility: bool
        """

        self._include_est_ctrl_compatibility = include_est_ctrl_compatibility

    @property
    def nadir_mode_in_eclipse(self):
        """Gets the nadir_mode_in_eclipse of this SimulationConfig.  # noqa: E501

        Switch to nadir mode during eclipse, when sun-pointing and not SimMode ADCS  # noqa: E501

        :return: The nadir_mode_in_eclipse of this SimulationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._nadir_mode_in_eclipse

    @nadir_mode_in_eclipse.setter
    def nadir_mode_in_eclipse(self, nadir_mode_in_eclipse):
        """Sets the nadir_mode_in_eclipse of this SimulationConfig.

        Switch to nadir mode during eclipse, when sun-pointing and not SimMode ADCS  # noqa: E501

        :param nadir_mode_in_eclipse: The nadir_mode_in_eclipse of this SimulationConfig.  # noqa: E501
        :type nadir_mode_in_eclipse: bool
        """

        self._nadir_mode_in_eclipse = nadir_mode_in_eclipse

    @property
    def mode_transition_threshold(self):
        """Gets the mode_transition_threshold of this SimulationConfig.  # noqa: E501

        [deg] when pointing error over sample period lower than this threshold after a mode transition, new mode is active and transition is completed  # noqa: E501

        :return: The mode_transition_threshold of this SimulationConfig.  # noqa: E501
        :rtype: float
        """
        return self._mode_transition_threshold

    @mode_transition_threshold.setter
    def mode_transition_threshold(self, mode_transition_threshold):
        """Sets the mode_transition_threshold of this SimulationConfig.

        [deg] when pointing error over sample period lower than this threshold after a mode transition, new mode is active and transition is completed  # noqa: E501

        :param mode_transition_threshold: The mode_transition_threshold of this SimulationConfig.  # noqa: E501
        :type mode_transition_threshold: float
        """

        self._mode_transition_threshold = mode_transition_threshold

    @property
    def mode_transition_samples(self):
        """Gets the mode_transition_samples of this SimulationConfig.  # noqa: E501

        number of samples for the above threshold (modeTransitionThreshold)  # noqa: E501

        :return: The mode_transition_samples of this SimulationConfig.  # noqa: E501
        :rtype: int
        """
        return self._mode_transition_samples

    @mode_transition_samples.setter
    def mode_transition_samples(self, mode_transition_samples):
        """Sets the mode_transition_samples of this SimulationConfig.

        number of samples for the above threshold (modeTransitionThreshold)  # noqa: E501

        :param mode_transition_samples: The mode_transition_samples of this SimulationConfig.  # noqa: E501
        :type mode_transition_samples: int
        """

        self._mode_transition_samples = mode_transition_samples

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SimulationConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationConfig):
            return True

        return self.to_dict() != other.to_dict()
