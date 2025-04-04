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


class EventFilter(object):
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
        '_property': 'str',
        'operator': 'str',
        'value': 'object'
    }

    attribute_map = {
        '_property': 'property',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, _property=None, operator=None, value=None, local_vars_configuration=None):  # noqa: E501
        """EventFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self.__property = None
        self._operator = None
        self._value = None
        self.discriminator = None

        self._property = _property
        self.operator = operator
        self.value = value

    @property
    def _property(self):
        """Gets the _property of this EventFilter.  # noqa: E501

        The property of the event to be filtered  # noqa: E501

        :return: The _property of this EventFilter.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this EventFilter.

        The property of the event to be filtered  # noqa: E501

        :param _property: The _property of this EventFilter.  # noqa: E501
        :type _property: str
        """
        if self.local_vars_configuration.client_side_validation and _property is None:  # noqa: E501
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

    @property
    def operator(self):
        """Gets the operator of this EventFilter.  # noqa: E501

        The operator to be used for filtering  # noqa: E501

        :return: The operator of this EventFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this EventFilter.

        The operator to be used for filtering  # noqa: E501

        :param operator: The operator of this EventFilter.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this EventFilter.  # noqa: E501

        The value to be used for filtering  # noqa: E501

        :return: The value of this EventFilter.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EventFilter.

        The value to be used for filtering  # noqa: E501

        :param value: The value of this EventFilter.  # noqa: E501
        :type value: object
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, EventFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventFilter):
            return True

        return self.to_dict() != other.to_dict()
