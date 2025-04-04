# coding: utf-8

"""
    EnduroSat SpaceOps REST API

    Documentation for EnduroSat SpaceOps REST API  # noqa: E501

    The version of the OpenAPI document: 0.34.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from endurosat_api.api_client import ApiClient
from endurosat_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ConjunctionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_filtered_conjunctions(self, **kwargs):  # noqa: E501
        """Get Conjunctions  # noqa: E501

        This method returns a filtered list of conjunctions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_filtered_conjunctions(async_req=True)
        >>> result = thread.get()

        :param conjunction_id: ID of the Conjunction
        :type conjunction_id: str
        :param satellite_id: ID of the satellite for which to get the conjunction
        :type satellite_id: str
        :param start_date: Start date for which to get the conjunction
        :type start_date: str
        :param end_date: End date for which to get the conjunction
        :type end_date: str
        :param collision_probability: The probability of the conjunction
        :type collision_probability: str
        :param page: Number of the page
        :type page: str
        :param per_page: Number of items per page
        :type per_page: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ConjunctionEvent
        """
        kwargs['_return_http_data_only'] = True
        return self.get_filtered_conjunctions_with_http_info(**kwargs)  # noqa: E501

    def get_filtered_conjunctions_with_http_info(self, **kwargs):  # noqa: E501
        """Get Conjunctions  # noqa: E501

        This method returns a filtered list of conjunctions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_filtered_conjunctions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param conjunction_id: ID of the Conjunction
        :type conjunction_id: str
        :param satellite_id: ID of the satellite for which to get the conjunction
        :type satellite_id: str
        :param start_date: Start date for which to get the conjunction
        :type start_date: str
        :param end_date: End date for which to get the conjunction
        :type end_date: str
        :param collision_probability: The probability of the conjunction
        :type collision_probability: str
        :param page: Number of the page
        :type page: str
        :param per_page: Number of items per page
        :type per_page: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ConjunctionEvent, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'conjunction_id',
            'satellite_id',
            'start_date',
            'end_date',
            'collision_probability',
            'page',
            'per_page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_filtered_conjunctions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conjunction_id' in local_var_params and local_var_params['conjunction_id'] is not None:  # noqa: E501
            query_params.append(('conjunction-id', local_var_params['conjunction_id']))  # noqa: E501
        if 'satellite_id' in local_var_params and local_var_params['satellite_id'] is not None:  # noqa: E501
            query_params.append(('satelliteId', local_var_params['satellite_id']))  # noqa: E501
        if 'start_date' in local_var_params and local_var_params['start_date'] is not None:  # noqa: E501
            query_params.append(('start-date', local_var_params['start_date']))  # noqa: E501
        if 'end_date' in local_var_params and local_var_params['end_date'] is not None:  # noqa: E501
            query_params.append(('end-date', local_var_params['end_date']))  # noqa: E501
        if 'collision_probability' in local_var_params and local_var_params['collision_probability'] is not None:  # noqa: E501
            query_params.append(('collision-probability', local_var_params['collision_probability']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per-page', local_var_params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['MyEnduroSat']  # noqa: E501
        
        response_types_map = {
            400: "ErrorResponse",
            200: "ConjunctionEvent",
            401: "ErrorResponse",
            403: "ErrorResponse",
        }

        return self.api_client.call_api(
            '/ca/conjunctions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
