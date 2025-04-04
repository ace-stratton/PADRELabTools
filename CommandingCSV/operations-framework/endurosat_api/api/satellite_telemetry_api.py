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


class SatelliteTelemetryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_filtered_telemetry_entries(self, **kwargs):  # noqa: E501
        """Get Historical Telemetry  # noqa: E501

        This method returns a filtered list of historical telemetry values for a satellite. Telemetry could be filtered by Satellite, Satellite Pass and time received  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_filtered_telemetry_entries(async_req=True)
        >>> result = thread.get()

        :param name: Specifies the name (or part of the name) of the telemetry
        :type name: str
        :param satellite_id: Specifies the satellite for which to get telemetry
        :type satellite_id: str
        :param satellite_subsystem_id: Specifies the satellite subsystem (or part of the subsytem) for which to get telemetry
        :type satellite_subsystem_id: str
        :param pass_id: Specifies the satellite pass (or part of the pass) during which telemetry was aquired
        :type pass_id: str
        :param from_time: Filter to only return entries that were received after the specified time (inclusive)
        :type from_time: int
        :param to_time: Filter to only return entries that were received before the specified time (exclusive)
        :type to_time: int
        :param mission_database: Filter by mission database (or part of the mission database)
        :type mission_database: str
        :param telecommand_request: Filter by telecommand request
        :type telecommand_request: str
        :param last_evaluated_item: Specified the ID of the last item that was returned from the last page
        :type last_evaluated_item: str
        :param page_size_limit: Specifies the maximum number of results per page. Defaults to 100
        :type page_size_limit: int
        :param data_query: Allows you to filter the data field using a query that supports the following comparison operations: '>' (greater than), '=='(equal to), '<'(less than), '>=' (greater than or equal to), '<=' (less than or equal to). Supported logical operators are 'and' and 'or'. Fields and values are case-sensitive. Example: fpHeader.SatId == 1 and (fpHeader.FuncId == 2 or fpHeader.FuncId == 3)
        :type data_query: str
        :param projection_expression: Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0]
        :type projection_expression: str
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
        :rtype: TelemetryResultPage
        """
        kwargs['_return_http_data_only'] = True
        return self.get_filtered_telemetry_entries_with_http_info(**kwargs)  # noqa: E501

    def get_filtered_telemetry_entries_with_http_info(self, **kwargs):  # noqa: E501
        """Get Historical Telemetry  # noqa: E501

        This method returns a filtered list of historical telemetry values for a satellite. Telemetry could be filtered by Satellite, Satellite Pass and time received  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_filtered_telemetry_entries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param name: Specifies the name (or part of the name) of the telemetry
        :type name: str
        :param satellite_id: Specifies the satellite for which to get telemetry
        :type satellite_id: str
        :param satellite_subsystem_id: Specifies the satellite subsystem (or part of the subsytem) for which to get telemetry
        :type satellite_subsystem_id: str
        :param pass_id: Specifies the satellite pass (or part of the pass) during which telemetry was aquired
        :type pass_id: str
        :param from_time: Filter to only return entries that were received after the specified time (inclusive)
        :type from_time: int
        :param to_time: Filter to only return entries that were received before the specified time (exclusive)
        :type to_time: int
        :param mission_database: Filter by mission database (or part of the mission database)
        :type mission_database: str
        :param telecommand_request: Filter by telecommand request
        :type telecommand_request: str
        :param last_evaluated_item: Specified the ID of the last item that was returned from the last page
        :type last_evaluated_item: str
        :param page_size_limit: Specifies the maximum number of results per page. Defaults to 100
        :type page_size_limit: int
        :param data_query: Allows you to filter the data field using a query that supports the following comparison operations: '>' (greater than), '=='(equal to), '<'(less than), '>=' (greater than or equal to), '<=' (less than or equal to). Supported logical operators are 'and' and 'or'. Fields and values are case-sensitive. Example: fpHeader.SatId == 1 and (fpHeader.FuncId == 2 or fpHeader.FuncId == 3)
        :type data_query: str
        :param projection_expression: Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0]
        :type projection_expression: str
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
        :rtype: tuple(TelemetryResultPage, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'name',
            'satellite_id',
            'satellite_subsystem_id',
            'pass_id',
            'from_time',
            'to_time',
            'mission_database',
            'telecommand_request',
            'last_evaluated_item',
            'page_size_limit',
            'data_query',
            'projection_expression'
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
                    " to method get_filtered_telemetry_entries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'satellite_id' in local_var_params and local_var_params['satellite_id'] is not None:  # noqa: E501
            query_params.append(('satelliteId', local_var_params['satellite_id']))  # noqa: E501
        if 'satellite_subsystem_id' in local_var_params and local_var_params['satellite_subsystem_id'] is not None:  # noqa: E501
            query_params.append(('satelliteSubsystemId', local_var_params['satellite_subsystem_id']))  # noqa: E501
        if 'pass_id' in local_var_params and local_var_params['pass_id'] is not None:  # noqa: E501
            query_params.append(('passId', local_var_params['pass_id']))  # noqa: E501
        if 'from_time' in local_var_params and local_var_params['from_time'] is not None:  # noqa: E501
            query_params.append(('fromTime', local_var_params['from_time']))  # noqa: E501
        if 'to_time' in local_var_params and local_var_params['to_time'] is not None:  # noqa: E501
            query_params.append(('toTime', local_var_params['to_time']))  # noqa: E501
        if 'mission_database' in local_var_params and local_var_params['mission_database'] is not None:  # noqa: E501
            query_params.append(('missionDatabase', local_var_params['mission_database']))  # noqa: E501
        if 'telecommand_request' in local_var_params and local_var_params['telecommand_request'] is not None:  # noqa: E501
            query_params.append(('telecommandRequest', local_var_params['telecommand_request']))  # noqa: E501
        if 'last_evaluated_item' in local_var_params and local_var_params['last_evaluated_item'] is not None:  # noqa: E501
            query_params.append(('lastEvaluatedItem', local_var_params['last_evaluated_item']))  # noqa: E501
        if 'page_size_limit' in local_var_params and local_var_params['page_size_limit'] is not None:  # noqa: E501
            query_params.append(('pageSizeLimit', local_var_params['page_size_limit']))  # noqa: E501
        if 'data_query' in local_var_params and local_var_params['data_query'] is not None:  # noqa: E501
            query_params.append(('dataQuery', local_var_params['data_query']))  # noqa: E501
        if 'projection_expression' in local_var_params and local_var_params['projection_expression'] is not None:  # noqa: E501
            query_params.append(('projectionExpression', local_var_params['projection_expression']))  # noqa: E501

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
            401: "ErrorResponse",
            403: "ErrorResponse",
            200: "TelemetryResultPage",
        }

        return self.api_client.call_api(
            '/satellite-telemetry', 'GET',
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

    def get_telemetry_entry_by_id(self, telemetry_entry_id, **kwargs):  # noqa: E501
        """Get a Satellite Telemetry Entry by ID  # noqa: E501

        This method returns a Satellite Telemetry Entry by ID for the current user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_telemetry_entry_by_id(telemetry_entry_id, async_req=True)
        >>> result = thread.get()

        :param telemetry_entry_id: ID of the Satellite Telemetry Entry to get (required)
        :type telemetry_entry_id: str
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
        :rtype: TelemetryEntry
        """
        kwargs['_return_http_data_only'] = True
        return self.get_telemetry_entry_by_id_with_http_info(telemetry_entry_id, **kwargs)  # noqa: E501

    def get_telemetry_entry_by_id_with_http_info(self, telemetry_entry_id, **kwargs):  # noqa: E501
        """Get a Satellite Telemetry Entry by ID  # noqa: E501

        This method returns a Satellite Telemetry Entry by ID for the current user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_telemetry_entry_by_id_with_http_info(telemetry_entry_id, async_req=True)
        >>> result = thread.get()

        :param telemetry_entry_id: ID of the Satellite Telemetry Entry to get (required)
        :type telemetry_entry_id: str
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
        :rtype: tuple(TelemetryEntry, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'telemetry_entry_id'
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
                    " to method get_telemetry_entry_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'telemetry_entry_id' is set
        if self.api_client.client_side_validation and ('telemetry_entry_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['telemetry_entry_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `telemetry_entry_id` when calling `get_telemetry_entry_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'telemetry_entry_id' in local_var_params:
            path_params['telemetryEntryId'] = local_var_params['telemetry_entry_id']  # noqa: E501

        query_params = []

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
            200: "TelemetryEntry",
            401: "ErrorResponse",
            403: "ErrorResponse",
            404: "ErrorResponse",
        }

        return self.api_client.call_api(
            '/satellite-telemetry/{telemetryEntryId}', 'GET',
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

    def record_batch_telemetry(self, telemetry_entry, **kwargs):  # noqa: E501
        """Record Batch Telemetry  # noqa: E501

        This method is used for recording batch telemetry for a satellite.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.record_batch_telemetry(telemetry_entry, async_req=True)
        >>> result = thread.get()

        :param telemetry_entry: (required)
        :type telemetry_entry: list[TelemetryEntry]
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.record_batch_telemetry_with_http_info(telemetry_entry, **kwargs)  # noqa: E501

    def record_batch_telemetry_with_http_info(self, telemetry_entry, **kwargs):  # noqa: E501
        """Record Batch Telemetry  # noqa: E501

        This method is used for recording batch telemetry for a satellite.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.record_batch_telemetry_with_http_info(telemetry_entry, async_req=True)
        >>> result = thread.get()

        :param telemetry_entry: (required)
        :type telemetry_entry: list[TelemetryEntry]
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'telemetry_entry'
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
                    " to method record_batch_telemetry" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'telemetry_entry' is set
        if self.api_client.client_side_validation and ('telemetry_entry' not in local_var_params or  # noqa: E501
                                                        local_var_params['telemetry_entry'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `telemetry_entry` when calling `record_batch_telemetry`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'telemetry_entry' in local_var_params:
            body_params = local_var_params['telemetry_entry']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['MyEnduroSat']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/satellite-telemetry/batch', 'POST',
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

    def record_telemetry_with_payload(self, payload, telemetry, **kwargs):  # noqa: E501
        """Record Telemetry with Payload  # noqa: E501

        This method is used for recording telemetry with a payload for a satellite.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.record_telemetry_with_payload(payload, telemetry, async_req=True)
        >>> result = thread.get()

        :param payload: (required)
        :type payload: file
        :param telemetry: (required)
        :type telemetry: TelemetryEntry
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.record_telemetry_with_payload_with_http_info(payload, telemetry, **kwargs)  # noqa: E501

    def record_telemetry_with_payload_with_http_info(self, payload, telemetry, **kwargs):  # noqa: E501
        """Record Telemetry with Payload  # noqa: E501

        This method is used for recording telemetry with a payload for a satellite.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.record_telemetry_with_payload_with_http_info(payload, telemetry, async_req=True)
        >>> result = thread.get()

        :param payload: (required)
        :type payload: file
        :param telemetry: (required)
        :type telemetry: TelemetryEntry
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'payload',
            'telemetry'
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
                    " to method record_telemetry_with_payload" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payload' is set
        if self.api_client.client_side_validation and ('payload' not in local_var_params or  # noqa: E501
                                                        local_var_params['payload'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payload` when calling `record_telemetry_with_payload`")  # noqa: E501
        # verify the required parameter 'telemetry' is set
        if self.api_client.client_side_validation and ('telemetry' not in local_var_params or  # noqa: E501
                                                        local_var_params['telemetry'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `telemetry` when calling `record_telemetry_with_payload`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'payload' in local_var_params:
            local_var_files['payload'] = local_var_params['payload']  # noqa: E501
        if 'telemetry' in local_var_params:
            form_params.append(('telemetry', local_var_params['telemetry']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['MyEnduroSat']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/satellite-telemetry/with-payload', 'POST',
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

    def update_telemetry_entry_by_id(self, telemetry_entry_id, telemetry_entry, **kwargs):  # noqa: E501
        """Update a Telemetry Entry  # noqa: E501

        This method updates a Telemetry Entry by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_telemetry_entry_by_id(telemetry_entry_id, telemetry_entry, async_req=True)
        >>> result = thread.get()

        :param telemetry_entry_id: ID of the Telemetry Entry to update (required)
        :type telemetry_entry_id: str
        :param telemetry_entry: (required)
        :type telemetry_entry: TelemetryEntry
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.update_telemetry_entry_by_id_with_http_info(telemetry_entry_id, telemetry_entry, **kwargs)  # noqa: E501

    def update_telemetry_entry_by_id_with_http_info(self, telemetry_entry_id, telemetry_entry, **kwargs):  # noqa: E501
        """Update a Telemetry Entry  # noqa: E501

        This method updates a Telemetry Entry by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_telemetry_entry_by_id_with_http_info(telemetry_entry_id, telemetry_entry, async_req=True)
        >>> result = thread.get()

        :param telemetry_entry_id: ID of the Telemetry Entry to update (required)
        :type telemetry_entry_id: str
        :param telemetry_entry: (required)
        :type telemetry_entry: TelemetryEntry
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'telemetry_entry_id',
            'telemetry_entry'
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
                    " to method update_telemetry_entry_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'telemetry_entry_id' is set
        if self.api_client.client_side_validation and ('telemetry_entry_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['telemetry_entry_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `telemetry_entry_id` when calling `update_telemetry_entry_by_id`")  # noqa: E501
        # verify the required parameter 'telemetry_entry' is set
        if self.api_client.client_side_validation and ('telemetry_entry' not in local_var_params or  # noqa: E501
                                                        local_var_params['telemetry_entry'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `telemetry_entry` when calling `update_telemetry_entry_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'telemetry_entry_id' in local_var_params:
            path_params['telemetryEntryId'] = local_var_params['telemetry_entry_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'telemetry_entry' in local_var_params:
            body_params = local_var_params['telemetry_entry']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['MyEnduroSat']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/satellite-telemetry/{telemetryEntryId}', 'PUT',
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
