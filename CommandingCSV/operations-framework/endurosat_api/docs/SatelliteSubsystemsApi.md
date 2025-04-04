# endurosat_api.SatelliteSubsystemsApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_satellite_subsystem**](SatelliteSubsystemsApi.md#create_satellite_subsystem) | **POST** /satellite-subsystems | Create a Satellite Subsystem
[**delete_satellite_subsystem_by_id**](SatelliteSubsystemsApi.md#delete_satellite_subsystem_by_id) | **DELETE** /satellite-subsystems/{satelliteSubsystemId} | Delete a Satellite Subsystem
[**get_filtered_satellite_subsystems**](SatelliteSubsystemsApi.md#get_filtered_satellite_subsystems) | **GET** /satellite-subsystems | Get all Satellite Subsystems
[**get_satellite_subsystem_by_id**](SatelliteSubsystemsApi.md#get_satellite_subsystem_by_id) | **GET** /satellite-subsystems/{satelliteSubsystemId} | Get a Satellite Subsystem by ID
[**update_satellite_subsystem_by_id**](SatelliteSubsystemsApi.md#update_satellite_subsystem_by_id) | **PUT** /satellite-subsystems/{satelliteSubsystemId} | Update a Satellite Subsystem


# **create_satellite_subsystem**
> create_satellite_subsystem(satellite_subsystem)

Create a Satellite Subsystem

This method creates a new Satellite Subsystem for the current user.

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
    api_instance = endurosat_api.SatelliteSubsystemsApi(api_client)
    satellite_subsystem = endurosat_api.SatelliteSubsystem() # SatelliteSubsystem | 

    try:
        # Create a Satellite Subsystem
        api_instance.create_satellite_subsystem(satellite_subsystem)
    except ApiException as e:
        print("Exception when calling SatelliteSubsystemsApi->create_satellite_subsystem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_subsystem** | [**SatelliteSubsystem**](SatelliteSubsystem.md)|  | 

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
**201** | Satellite Subsystem created successfully |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_satellite_subsystem_by_id**
> delete_satellite_subsystem_by_id(satellite_subsystem_id)

Delete a Satellite Subsystem

This method deletes a Satellite Subsystem by ID

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
    api_instance = endurosat_api.SatelliteSubsystemsApi(api_client)
    satellite_subsystem_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Subsystem to delete

    try:
        # Delete a Satellite Subsystem
        api_instance.delete_satellite_subsystem_by_id(satellite_subsystem_id)
    except ApiException as e:
        print("Exception when calling SatelliteSubsystemsApi->delete_satellite_subsystem_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_subsystem_id** | **str**| ID of the Satellite Subsystem to delete | 

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

# **get_filtered_satellite_subsystems**
> list[SatelliteSubsystem] get_filtered_satellite_subsystems(satellite_id=satellite_id, name=name, type=type)

Get all Satellite Subsystems

This method returns a filtered list of Satellite Subsystems. Satellite Subsystems could be filtered by Satellite, Name and Type. Maximum count of the returned items is 10000.

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
    api_instance = endurosat_api.SatelliteSubsystemsApi(api_client)
    satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the Satellite for which the Subsystems are applicable (optional)
name = 'UHF Antenna' # str | Specifies the name (or part of the name) of the Subsystem (optional)
type = 'UHF' # str | Specifies the type (or part of the type) of the Subsystem (optional)

    try:
        # Get all Satellite Subsystems
        api_response = api_instance.get_filtered_satellite_subsystems(satellite_id=satellite_id, name=name, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteSubsystemsApi->get_filtered_satellite_subsystems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_id** | **str**| Specifies the Satellite for which the Subsystems are applicable | [optional] 
 **name** | **str**| Specifies the name (or part of the name) of the Subsystem | [optional] 
 **type** | **str**| Specifies the type (or part of the type) of the Subsystem | [optional] 

### Return type

[**list[SatelliteSubsystem]**](SatelliteSubsystem.md)

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

# **get_satellite_subsystem_by_id**
> SatelliteSubsystem get_satellite_subsystem_by_id(satellite_subsystem_id)

Get a Satellite Subsystem by ID

This method returns a Satellite Subsystem by ID

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
    api_instance = endurosat_api.SatelliteSubsystemsApi(api_client)
    satellite_subsystem_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Subsystem to get

    try:
        # Get a Satellite Subsystem by ID
        api_response = api_instance.get_satellite_subsystem_by_id(satellite_subsystem_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteSubsystemsApi->get_satellite_subsystem_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_subsystem_id** | **str**| ID of the Satellite Subsystem to get | 

### Return type

[**SatelliteSubsystem**](SatelliteSubsystem.md)

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_satellite_subsystem_by_id**
> update_satellite_subsystem_by_id(satellite_subsystem_id, satellite_subsystem)

Update a Satellite Subsystem

This method updates a Satellite Subsystem by ID

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
    api_instance = endurosat_api.SatelliteSubsystemsApi(api_client)
    satellite_subsystem_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Subsystem to update
satellite_subsystem = endurosat_api.SatelliteSubsystem() # SatelliteSubsystem | 

    try:
        # Update a Satellite Subsystem
        api_instance.update_satellite_subsystem_by_id(satellite_subsystem_id, satellite_subsystem)
    except ApiException as e:
        print("Exception when calling SatelliteSubsystemsApi->update_satellite_subsystem_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_subsystem_id** | **str**| ID of the Satellite Subsystem to update | 
 **satellite_subsystem** | [**SatelliteSubsystem**](SatelliteSubsystem.md)|  | 

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

