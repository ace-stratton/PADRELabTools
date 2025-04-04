# endurosat_api.SatelliteTelecommandsApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_telecommand**](SatelliteTelecommandsApi.md#create_telecommand) | **POST** /satellite-telecommands | Create a Satellite Telecommand
[**create_telecommand_with_payload**](SatelliteTelecommandsApi.md#create_telecommand_with_payload) | **POST** /satellite-telecommands/with-payload | Create a Satellite Telecommand with Payload
[**delete_telecommand_by_id**](SatelliteTelecommandsApi.md#delete_telecommand_by_id) | **DELETE** /satellite-telecommands/{telecommandId} | Delete a Satellite Telecommand
[**get_executed_telecommands**](SatelliteTelecommandsApi.md#get_executed_telecommands) | **GET** /satellite-telecommands/history | Get Telecommand History
[**get_filtered_telecommands**](SatelliteTelecommandsApi.md#get_filtered_telecommands) | **GET** /satellite-telecommands | Get Filtered Telecommands
[**get_regular_telecommands**](SatelliteTelecommandsApi.md#get_regular_telecommands) | **GET** /satellite-telecommands/pending-regular | Get Regular Telecommands
[**get_telecommand_by_id**](SatelliteTelecommandsApi.md#get_telecommand_by_id) | **GET** /satellite-telecommands/{telecommandId} | Get a Satellite Telecommand by ID
[**get_time_tagged_telecommands**](SatelliteTelecommandsApi.md#get_time_tagged_telecommands) | **GET** /satellite-telecommands/pending-time-tagged | Get TimeTagged Telecommands
[**update_telecommand_by_id**](SatelliteTelecommandsApi.md#update_telecommand_by_id) | **PUT** /satellite-telecommands/{telecommandId} | Update a Satellite Telecommand


# **create_telecommand**
> str create_telecommand(telecommand)

Create a Satellite Telecommand

This method creates new satellite telecommands for the current user.

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    telecommand = endurosat_api.Telecommand() # Telecommand | 

    try:
        # Create a Satellite Telecommand
        api_response = api_instance.create_telecommand(telecommand)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->create_telecommand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telecommand** | [**Telecommand**](Telecommand.md)|  | 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**201** | Satellite Telecommand created successfully |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_telecommand_with_payload**
> str create_telecommand_with_payload(payload, telecommand)

Create a Satellite Telecommand with Payload

This method creates new satellite telecommands with payloads for the current user.

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    payload = '/path/to/file' # file | 
telecommand = endurosat_api.Telecommand() # Telecommand | 

    try:
        # Create a Satellite Telecommand with Payload
        api_response = api_instance.create_telecommand_with_payload(payload, telecommand)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->create_telecommand_with_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | **file**|  | 
 **telecommand** | [**Telecommand**](Telecommand.md)|  | 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**201** | Satellite Telecommand created successfully |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_telecommand_by_id**
> delete_telecommand_by_id(telecommand_id)

Delete a Satellite Telecommand

This method deletes a Satellite Telecommand by ID for the current user

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    telecommand_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Telecommand to delete

    try:
        # Delete a Satellite Telecommand
        api_instance.delete_telecommand_by_id(telecommand_id)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->delete_telecommand_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telecommand_id** | **str**| ID of the Satellite Telecommand to delete | 

### Return type

void (empty response body)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**404** | Not Found - A requested resource was not found |  -  |
**204** | No Content - Request was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executed_telecommands**
> TelecommandsResultPage get_executed_telecommands(satellite_id=satellite_id, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)

Get Telecommand History

This method returns a list of already executed telecommands for a satellite. Telecommands could be filtered by Satellite, FromTime, ToTime based on their execution time.

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite for which to get telecommands (optional)
from_time = 56 # int | Filter to only return entries that were received after the specified time (inclusive) (optional)
to_time = 56 # int | Filter to only return entries that were received before the specified time (exclusive) (optional)
last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)
data_query = 'data_query_example' # str | Allows you to filter the data field using a query that supports the following comparison operations: '>' (greater than), '=='(equal to), '<'(less than), '>=' (greater than or equal to), '<=' (less than or equal to). Supported logical operators are 'and' and 'or'. Fields and values are case-sensitive. Example: fpHeader.SatId == 1 and (fpHeader.FuncId == 2 or fpHeader.FuncId == 3) (optional)
projection_expression = 'projection_expression_example' # str | Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] (optional)

    try:
        # Get Telecommand History
        api_response = api_instance.get_executed_telecommands(satellite_id=satellite_id, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->get_executed_telecommands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_id** | **str**| Specifies the satellite for which to get telecommands | [optional] 
 **from_time** | **int**| Filter to only return entries that were received after the specified time (inclusive) | [optional] 
 **to_time** | **int**| Filter to only return entries that were received before the specified time (exclusive) | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 
 **data_query** | **str**| Allows you to filter the data field using a query that supports the following comparison operations: &#39;&gt;&#39; (greater than), &#39;&#x3D;&#x3D;&#39;(equal to), &#39;&lt;&#39;(less than), &#39;&gt;&#x3D;&#39; (greater than or equal to), &#39;&lt;&#x3D;&#39; (less than or equal to). Supported logical operators are &#39;and&#39; and &#39;or&#39;. Fields and values are case-sensitive. Example: fpHeader.SatId &#x3D;&#x3D; 1 and (fpHeader.FuncId &#x3D;&#x3D; 2 or fpHeader.FuncId &#x3D;&#x3D; 3) | [optional] 
 **projection_expression** | **str**| Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] | [optional] 

### Return type

[**TelecommandsResultPage**](TelecommandsResultPage.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_telecommands**
> TelecommandsResultPage get_filtered_telecommands(satellite_id=satellite_id, satellite_subsystem_id=satellite_subsystem_id, name=name, requested_satellite_pass=requested_satellite_pass, executed_satellite_pass=executed_satellite_pass, status=status, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)

Get Filtered Telecommands

This method returns a filtered list of telecommands for a satellite. Telecommands could be filtered by Satellite, Satellite Subsystem, Requested Satellite Pass, Executed Satellite Pass and Status

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite for which to get telecommands (optional)
satellite_subsystem_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite subsystem (or part of the subsystem) for which to get telecommands (optional)
name = 'Raise' # str | Specifies the name or part of the name (or part of the name) of the telecommand (optional)
requested_satellite_pass = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite pass (or part of the pass) for which the telecommand was originally scheduled (optional)
executed_satellite_pass = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite pass (or part of the pass) during which the telecommand was sent to the satellite (optional)
status = 'status_example' # str | Specifies the status (or part of the status) of the telecommand (optional)
last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)
data_query = 'data_query_example' # str | Allows you to filter the data field using a query that supports the following comparison operations: '>' (greater than), '=='(equal to), '<'(less than), '>=' (greater than or equal to), '<=' (less than or equal to). Supported logical operators are 'and' and 'or'. Fields and values are case-sensitive. Example: fpHeader.SatId == 1 and (fpHeader.FuncId == 2 or fpHeader.FuncId == 3) (optional)
projection_expression = 'projection_expression_example' # str | Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] (optional)

    try:
        # Get Filtered Telecommands
        api_response = api_instance.get_filtered_telecommands(satellite_id=satellite_id, satellite_subsystem_id=satellite_subsystem_id, name=name, requested_satellite_pass=requested_satellite_pass, executed_satellite_pass=executed_satellite_pass, status=status, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->get_filtered_telecommands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_id** | **str**| Specifies the satellite for which to get telecommands | [optional] 
 **satellite_subsystem_id** | **str**| Specifies the satellite subsystem (or part of the subsystem) for which to get telecommands | [optional] 
 **name** | **str**| Specifies the name or part of the name (or part of the name) of the telecommand | [optional] 
 **requested_satellite_pass** | **str**| Specifies the satellite pass (or part of the pass) for which the telecommand was originally scheduled | [optional] 
 **executed_satellite_pass** | **str**| Specifies the satellite pass (or part of the pass) during which the telecommand was sent to the satellite | [optional] 
 **status** | **str**| Specifies the status (or part of the status) of the telecommand | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 
 **data_query** | **str**| Allows you to filter the data field using a query that supports the following comparison operations: &#39;&gt;&#39; (greater than), &#39;&#x3D;&#x3D;&#39;(equal to), &#39;&lt;&#39;(less than), &#39;&gt;&#x3D;&#39; (greater than or equal to), &#39;&lt;&#x3D;&#39; (less than or equal to). Supported logical operators are &#39;and&#39; and &#39;or&#39;. Fields and values are case-sensitive. Example: fpHeader.SatId &#x3D;&#x3D; 1 and (fpHeader.FuncId &#x3D;&#x3D; 2 or fpHeader.FuncId &#x3D;&#x3D; 3) | [optional] 
 **projection_expression** | **str**| Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] | [optional] 

### Return type

[**TelecommandsResultPage**](TelecommandsResultPage.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regular_telecommands**
> TelecommandsResultPage get_regular_telecommands(satellite_id=satellite_id, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)

Get Regular Telecommands

This method returns a list of regular telecommands for a satellite that are not executed yet. Telecommands could be filtered by Satellite, FromTime, ToTime based on their requested pass AOS.

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite for which to get telecommands (optional)
from_time = 56 # int | Filter to only return entries that were received after the specified time (inclusive) (optional)
to_time = 56 # int | Filter to only return entries that were received before the specified time (exclusive) (optional)
last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)
data_query = 'data_query_example' # str | Allows you to filter the data field using a query that supports the following comparison operations: '>' (greater than), '=='(equal to), '<'(less than), '>=' (greater than or equal to), '<=' (less than or equal to). Supported logical operators are 'and' and 'or'. Fields and values are case-sensitive. Example: fpHeader.SatId == 1 and (fpHeader.FuncId == 2 or fpHeader.FuncId == 3) (optional)
projection_expression = 'projection_expression_example' # str | Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] (optional)

    try:
        # Get Regular Telecommands
        api_response = api_instance.get_regular_telecommands(satellite_id=satellite_id, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->get_regular_telecommands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_id** | **str**| Specifies the satellite for which to get telecommands | [optional] 
 **from_time** | **int**| Filter to only return entries that were received after the specified time (inclusive) | [optional] 
 **to_time** | **int**| Filter to only return entries that were received before the specified time (exclusive) | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 
 **data_query** | **str**| Allows you to filter the data field using a query that supports the following comparison operations: &#39;&gt;&#39; (greater than), &#39;&#x3D;&#x3D;&#39;(equal to), &#39;&lt;&#39;(less than), &#39;&gt;&#x3D;&#39; (greater than or equal to), &#39;&lt;&#x3D;&#39; (less than or equal to). Supported logical operators are &#39;and&#39; and &#39;or&#39;. Fields and values are case-sensitive. Example: fpHeader.SatId &#x3D;&#x3D; 1 and (fpHeader.FuncId &#x3D;&#x3D; 2 or fpHeader.FuncId &#x3D;&#x3D; 3) | [optional] 
 **projection_expression** | **str**| Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] | [optional] 

### Return type

[**TelecommandsResultPage**](TelecommandsResultPage.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telecommand_by_id**
> Telecommand get_telecommand_by_id(telecommand_id)

Get a Satellite Telecommand by ID

This method returns a Satellite Telecommand by ID for the current user

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    telecommand_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Telecommand to get

    try:
        # Get a Satellite Telecommand by ID
        api_response = api_instance.get_telecommand_by_id(telecommand_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->get_telecommand_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telecommand_id** | **str**| ID of the Satellite Telecommand to get | 

### Return type

[**Telecommand**](Telecommand.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**200** | Successful response |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**404** | Not Found - A requested resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tagged_telecommands**
> TelecommandsResultPage get_time_tagged_telecommands(satellite_id=satellite_id, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)

Get TimeTagged Telecommands

This method returns a list of time tagged telecommands for a satellite that are not executed yet. Telecommands could be filtered by Satellite, FromTime, ToTime based on their start of satellite command execution.

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite for which to get telecommands (optional)
from_time = 56 # int | Filter to only return entries that were received after the specified time (inclusive) (optional)
to_time = 56 # int | Filter to only return entries that were received before the specified time (exclusive) (optional)
last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)
data_query = 'data_query_example' # str | Allows you to filter the data field using a query that supports the following comparison operations: '>' (greater than), '=='(equal to), '<'(less than), '>=' (greater than or equal to), '<=' (less than or equal to). Supported logical operators are 'and' and 'or'. Fields and values are case-sensitive. Example: fpHeader.SatId == 1 and (fpHeader.FuncId == 2 or fpHeader.FuncId == 3) (optional)
projection_expression = 'projection_expression_example' # str | Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] (optional)

    try:
        # Get TimeTagged Telecommands
        api_response = api_instance.get_time_tagged_telecommands(satellite_id=satellite_id, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->get_time_tagged_telecommands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_id** | **str**| Specifies the satellite for which to get telecommands | [optional] 
 **from_time** | **int**| Filter to only return entries that were received after the specified time (inclusive) | [optional] 
 **to_time** | **int**| Filter to only return entries that were received before the specified time (exclusive) | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 
 **data_query** | **str**| Allows you to filter the data field using a query that supports the following comparison operations: &#39;&gt;&#39; (greater than), &#39;&#x3D;&#x3D;&#39;(equal to), &#39;&lt;&#39;(less than), &#39;&gt;&#x3D;&#39; (greater than or equal to), &#39;&lt;&#x3D;&#39; (less than or equal to). Supported logical operators are &#39;and&#39; and &#39;or&#39;. Fields and values are case-sensitive. Example: fpHeader.SatId &#x3D;&#x3D; 1 and (fpHeader.FuncId &#x3D;&#x3D; 2 or fpHeader.FuncId &#x3D;&#x3D; 3) | [optional] 
 **projection_expression** | **str**| Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] | [optional] 

### Return type

[**TelecommandsResultPage**](TelecommandsResultPage.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telecommand_by_id**
> update_telecommand_by_id(telecommand_id, telecommand)

Update a Satellite Telecommand

This method updates a Satellite Telecommand by ID for the current user

### Example

* OAuth Authentication (MyEnduroSat):
```python
from __future__ import print_function
import time
import endurosat_api
from endurosat_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ground-station.endurosat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: MyEnduroSat
configuration = endurosat_api.Configuration(
    host = "https://api.ground-station.endurosat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with endurosat_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.SatelliteTelecommandsApi(api_client)
    telecommand_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Telecommand to update
telecommand = endurosat_api.Telecommand() # Telecommand | 

    try:
        # Update a Satellite Telecommand
        api_instance.update_telecommand_by_id(telecommand_id, telecommand)
    except ApiException as e:
        print("Exception when calling SatelliteTelecommandsApi->update_telecommand_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telecommand_id** | **str**| ID of the Satellite Telecommand to update | 
 **telecommand** | [**Telecommand**](Telecommand.md)|  | 

### Return type

void (empty response body)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**404** | Not Found - A requested resource was not found |  -  |
**204** | No Content - Request was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

