# endurosat_api.SatelliteTelemetryApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filtered_telemetry_entries**](SatelliteTelemetryApi.md#get_filtered_telemetry_entries) | **GET** /satellite-telemetry | Get Historical Telemetry
[**get_telemetry_entry_by_id**](SatelliteTelemetryApi.md#get_telemetry_entry_by_id) | **GET** /satellite-telemetry/{telemetryEntryId} | Get a Satellite Telemetry Entry by ID
[**record_batch_telemetry**](SatelliteTelemetryApi.md#record_batch_telemetry) | **POST** /satellite-telemetry/batch | Record Batch Telemetry
[**record_telemetry_with_payload**](SatelliteTelemetryApi.md#record_telemetry_with_payload) | **POST** /satellite-telemetry/with-payload | Record Telemetry with Payload
[**update_telemetry_entry_by_id**](SatelliteTelemetryApi.md#update_telemetry_entry_by_id) | **PUT** /satellite-telemetry/{telemetryEntryId} | Update a Telemetry Entry


# **get_filtered_telemetry_entries**
> TelemetryResultPage get_filtered_telemetry_entries(name=name, satellite_id=satellite_id, satellite_subsystem_id=satellite_subsystem_id, pass_id=pass_id, from_time=from_time, to_time=to_time, mission_database=mission_database, telecommand_request=telecommand_request, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)

Get Historical Telemetry

This method returns a filtered list of historical telemetry values for a satellite. Telemetry could be filtered by Satellite, Satellite Pass and time received

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
    api_instance = endurosat_api.SatelliteTelemetryApi(api_client)
    name = 'Beacon' # str | Specifies the name (or part of the name) of the telemetry (optional)
satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite for which to get telemetry (optional)
satellite_subsystem_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite subsystem (or part of the subsytem) for which to get telemetry (optional)
pass_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite pass (or part of the pass) during which telemetry was aquired (optional)
from_time = 56 # int | Filter to only return entries that were received after the specified time (inclusive) (optional)
to_time = 56 # int | Filter to only return entries that were received before the specified time (exclusive) (optional)
mission_database = 'mission_database_example' # str | Filter by mission database (or part of the mission database) (optional)
telecommand_request = 'telecommand_request_example' # str | Filter by telecommand request (optional)
last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)
data_query = 'data_query_example' # str | Allows you to filter the data field using a query that supports the following comparison operations: '>' (greater than), '=='(equal to), '<'(less than), '>=' (greater than or equal to), '<=' (less than or equal to). Supported logical operators are 'and' and 'or'. Fields and values are case-sensitive. Example: fpHeader.SatId == 1 and (fpHeader.FuncId == 2 or fpHeader.FuncId == 3) (optional)
projection_expression = 'projection_expression_example' # str | Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] (optional)

    try:
        # Get Historical Telemetry
        api_response = api_instance.get_filtered_telemetry_entries(name=name, satellite_id=satellite_id, satellite_subsystem_id=satellite_subsystem_id, pass_id=pass_id, from_time=from_time, to_time=to_time, mission_database=mission_database, telecommand_request=telecommand_request, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit, data_query=data_query, projection_expression=projection_expression)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelemetryApi->get_filtered_telemetry_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name (or part of the name) of the telemetry | [optional] 
 **satellite_id** | **str**| Specifies the satellite for which to get telemetry | [optional] 
 **satellite_subsystem_id** | **str**| Specifies the satellite subsystem (or part of the subsytem) for which to get telemetry | [optional] 
 **pass_id** | **str**| Specifies the satellite pass (or part of the pass) during which telemetry was aquired | [optional] 
 **from_time** | **int**| Filter to only return entries that were received after the specified time (inclusive) | [optional] 
 **to_time** | **int**| Filter to only return entries that were received before the specified time (exclusive) | [optional] 
 **mission_database** | **str**| Filter by mission database (or part of the mission database) | [optional] 
 **telecommand_request** | **str**| Filter by telecommand request | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 
 **data_query** | **str**| Allows you to filter the data field using a query that supports the following comparison operations: &#39;&gt;&#39; (greater than), &#39;&#x3D;&#x3D;&#39;(equal to), &#39;&lt;&#39;(less than), &#39;&gt;&#x3D;&#39; (greater than or equal to), &#39;&lt;&#x3D;&#39; (less than or equal to). Supported logical operators are &#39;and&#39; and &#39;or&#39;. Fields and values are case-sensitive. Example: fpHeader.SatId &#x3D;&#x3D; 1 and (fpHeader.FuncId &#x3D;&#x3D; 2 or fpHeader.FuncId &#x3D;&#x3D; 3) | [optional] 
 **projection_expression** | **str**| Allows you to specify a subset of attributes to be returned. By default, all attributes are returned. Projection expression supports all properties of the data field. Example: fpHeader.SatId, fpHeader.FuncId, data.types[0] | [optional] 

### Return type

[**TelemetryResultPage**](TelemetryResultPage.md)

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

# **get_telemetry_entry_by_id**
> TelemetryEntry get_telemetry_entry_by_id(telemetry_entry_id)

Get a Satellite Telemetry Entry by ID

This method returns a Satellite Telemetry Entry by ID for the current user

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
    api_instance = endurosat_api.SatelliteTelemetryApi(api_client)
    telemetry_entry_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Telemetry Entry to get

    try:
        # Get a Satellite Telemetry Entry by ID
        api_response = api_instance.get_telemetry_entry_by_id(telemetry_entry_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteTelemetryApi->get_telemetry_entry_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_entry_id** | **str**| ID of the Satellite Telemetry Entry to get | 

### Return type

[**TelemetryEntry**](TelemetryEntry.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**200** | Successful response |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**404** | Not Found - A requested resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_batch_telemetry**
> record_batch_telemetry(telemetry_entry)

Record Batch Telemetry

This method is used for recording batch telemetry for a satellite.

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
    api_instance = endurosat_api.SatelliteTelemetryApi(api_client)
    telemetry_entry = [endurosat_api.TelemetryEntry()] # list[TelemetryEntry] | 

    try:
        # Record Batch Telemetry
        api_instance.record_batch_telemetry(telemetry_entry)
    except ApiException as e:
        print("Exception when calling SatelliteTelemetryApi->record_batch_telemetry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_entry** | [**list[TelemetryEntry]**](TelemetryEntry.md)|  | 

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
**201** | Telemetry recorded successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_telemetry_with_payload**
> record_telemetry_with_payload(payload, telemetry)

Record Telemetry with Payload

This method is used for recording telemetry with a payload for a satellite.

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
    api_instance = endurosat_api.SatelliteTelemetryApi(api_client)
    payload = '/path/to/file' # file | 
telemetry = endurosat_api.TelemetryEntry() # TelemetryEntry | 

    try:
        # Record Telemetry with Payload
        api_instance.record_telemetry_with_payload(payload, telemetry)
    except ApiException as e:
        print("Exception when calling SatelliteTelemetryApi->record_telemetry_with_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | **file**|  | 
 **telemetry** | [**TelemetryEntry**](TelemetryEntry.md)|  | 

### Return type

void (empty response body)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**201** | Telemetry recorded successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telemetry_entry_by_id**
> update_telemetry_entry_by_id(telemetry_entry_id, telemetry_entry)

Update a Telemetry Entry

This method updates a Telemetry Entry by ID

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
    api_instance = endurosat_api.SatelliteTelemetryApi(api_client)
    telemetry_entry_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Telemetry Entry to update
telemetry_entry = endurosat_api.TelemetryEntry() # TelemetryEntry | 

    try:
        # Update a Telemetry Entry
        api_instance.update_telemetry_entry_by_id(telemetry_entry_id, telemetry_entry)
    except ApiException as e:
        print("Exception when calling SatelliteTelemetryApi->update_telemetry_entry_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_entry_id** | **str**| ID of the Telemetry Entry to update | 
 **telemetry_entry** | [**TelemetryEntry**](TelemetryEntry.md)|  | 

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

