# endurosat_api.GroundStationsApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_unavailability_windows_by_ground_station_by_id**](GroundStationsApi.md#add_unavailability_windows_by_ground_station_by_id) | **PATCH** /ground-stations/{groundStationId}/unavailability-windows | Add an Unavailability Window to a Ground Station
[**create_ground_station**](GroundStationsApi.md#create_ground_station) | **POST** /ground-stations | Create a new Ground Station
[**delete_ground_station**](GroundStationsApi.md#delete_ground_station) | **DELETE** /ground-stations/{groundStationId} | Delete a Ground Station by ID
[**delete_unavailability_window**](GroundStationsApi.md#delete_unavailability_window) | **DELETE** /ground-stations/{groundStationId}/unavailability-windows/{unavailabilityWindowId} | Delete an Unavailability Window from a Ground Station
[**get_all_ground_stations**](GroundStationsApi.md#get_all_ground_stations) | **GET** /ground-stations | Get all Ground Stations
[**get_ground_station_by_id**](GroundStationsApi.md#get_ground_station_by_id) | **GET** /ground-stations/{groundStationId} | Get a Ground Station by ID
[**get_unavailability_windows_by_ground_station_by_id**](GroundStationsApi.md#get_unavailability_windows_by_ground_station_by_id) | **GET** /ground-stations/{groundStationId}/unavailability-windows | Get all Unavailability Windowss for a Ground Station
[**update_ground_station**](GroundStationsApi.md#update_ground_station) | **PUT** /ground-stations/{groundStationId} | Update a Ground Station


# **add_unavailability_windows_by_ground_station_by_id**
> add_unavailability_windows_by_ground_station_by_id(ground_station_id, unavailability_window)

Add an Unavailability Window to a Ground Station

This method adds an Unavailability Window to a specified Ground Station

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    ground_station_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Ground Station for which add Unavailability Windows
unavailability_window = endurosat_api.UnavailabilityWindow() # UnavailabilityWindow | 

    try:
        # Add an Unavailability Window to a Ground Station
        api_instance.add_unavailability_windows_by_ground_station_by_id(ground_station_id, unavailability_window)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->add_unavailability_windows_by_ground_station_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station_id** | **str**| ID of the Ground Station for which add Unavailability Windows | 
 **unavailability_window** | [**UnavailabilityWindow**](UnavailabilityWindow.md)|  | 

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
**201** | Unavailability Window added successfully |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ground_station**
> create_ground_station(ground_station)

Create a new Ground Station

This method creates a new Ground Stations

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    ground_station = endurosat_api.GroundStation() # GroundStation | 

    try:
        # Create a new Ground Station
        api_instance.create_ground_station(ground_station)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->create_ground_station: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station** | [**GroundStation**](GroundStation.md)|  | 

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
**201** | Ground Station Created Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ground_station**
> delete_ground_station(ground_station_id)

Delete a Ground Station by ID

This method deletes a Ground Station with the specified ID

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    ground_station_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Ground Station to delete

    try:
        # Delete a Ground Station by ID
        api_instance.delete_ground_station(ground_station_id)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->delete_ground_station: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station_id** | **str**| ID of the Ground Station to delete | 

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

# **delete_unavailability_window**
> delete_unavailability_window(ground_station_id, unavailability_window_id)

Delete an Unavailability Window from a Ground Station

This method deletes an Unavailability Window from a specified Ground Station

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    ground_station_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Ground Station for which delete Unavailability Windows
unavailability_window_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Unavailability Window to delete

    try:
        # Delete an Unavailability Window from a Ground Station
        api_instance.delete_unavailability_window(ground_station_id, unavailability_window_id)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->delete_unavailability_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station_id** | **str**| ID of the Ground Station for which delete Unavailability Windows | 
 **unavailability_window_id** | **str**| ID of the Unavailability Window to delete | 

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

# **get_all_ground_stations**
> list[GroundStation] get_all_ground_stations()

Get all Ground Stations

This method returns a list of all Ground Stations

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    
    try:
        # Get all Ground Stations
        api_response = api_instance.get_all_ground_stations()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->get_all_ground_stations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GroundStation]**](GroundStation.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ground_station_by_id**
> GroundStation get_ground_station_by_id(ground_station_id)

Get a Ground Station by ID

This method returns a Ground Station by ID

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    ground_station_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Ground Station to get

    try:
        # Get a Ground Station by ID
        api_response = api_instance.get_ground_station_by_id(ground_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->get_ground_station_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station_id** | **str**| ID of the Ground Station to get | 

### Return type

[**GroundStation**](GroundStation.md)

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

# **get_unavailability_windows_by_ground_station_by_id**
> list[UnavailabilityWindow] get_unavailability_windows_by_ground_station_by_id(ground_station_id)

Get all Unavailability Windowss for a Ground Station

This method returns a list of all Unavailability Windows for a specified Ground Station

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    ground_station_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Ground Station for which to return Unavailability Windows

    try:
        # Get all Unavailability Windowss for a Ground Station
        api_response = api_instance.get_unavailability_windows_by_ground_station_by_id(ground_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->get_unavailability_windows_by_ground_station_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station_id** | **str**| ID of the Ground Station for which to return Unavailability Windows | 

### Return type

[**list[UnavailabilityWindow]**](UnavailabilityWindow.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ground_station**
> update_ground_station(ground_station_id, ground_station)

Update a Ground Station

This method updates a Ground Station by ID

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
    api_instance = endurosat_api.GroundStationsApi(api_client)
    ground_station_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Ground Station to update
ground_station = endurosat_api.GroundStation() # GroundStation | 

    try:
        # Update a Ground Station
        api_instance.update_ground_station(ground_station_id, ground_station)
    except ApiException as e:
        print("Exception when calling GroundStationsApi->update_ground_station: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station_id** | **str**| ID of the Ground Station to update | 
 **ground_station** | [**GroundStation**](GroundStation.md)|  | 

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

