# endurosat_api.SatellitePassesApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_satellite_pass**](SatellitePassesApi.md#cancel_satellite_pass) | **DELETE** /satellite-passes/{satellitePassId} | Cancel a Satellite Pass
[**create_satellite_pass**](SatellitePassesApi.md#create_satellite_pass) | **POST** /satellite-passes | Book a Satellite Pass
[**get_filtered_satellite_passes**](SatellitePassesApi.md#get_filtered_satellite_passes) | **GET** /satellite-passes | Get Filtered Satellite Passes
[**get_satellite_pass_by_id**](SatellitePassesApi.md#get_satellite_pass_by_id) | **GET** /satellite-passes/{satellitePassId} | Get a Satellite Pass by ID
[**record_satellite_pass_artifact**](SatellitePassesApi.md#record_satellite_pass_artifact) | **POST** /satellite-passes/{satellitePassId}/artifacts/{artifactType} | Record a Satellite Pass Artifact
[**record_satellite_pass_log**](SatellitePassesApi.md#record_satellite_pass_log) | **POST** /satellite-passes/{satellitePassId}/log | Record a Satellite Pass Log
[**update_satellite_pass_by_id**](SatellitePassesApi.md#update_satellite_pass_by_id) | **PUT** /satellite-passes/{satellitePassId} | Update a Satellite Pass


# **cancel_satellite_pass**
> cancel_satellite_pass(satellite_pass_id)

Cancel a Satellite Pass

This method cancels a satellite pass by ID for the current user

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
    api_instance = endurosat_api.SatellitePassesApi(api_client)
    satellite_pass_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Pass to delete

    try:
        # Cancel a Satellite Pass
        api_instance.cancel_satellite_pass(satellite_pass_id)
    except ApiException as e:
        print("Exception when calling SatellitePassesApi->cancel_satellite_pass: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_pass_id** | **str**| ID of the Satellite Pass to delete | 

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

# **create_satellite_pass**
> str create_satellite_pass(pass_prediction)

Book a Satellite Pass

This method is used for booking passes for the current user. It requires a Pass Prediction obtained from the Pass Prediction API to be provided in the body of the request. Pass predictions are valid for 20 minutes.If the prediction has expired or is ivalid, a 400 Bad Request response will be returned.

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
    api_instance = endurosat_api.SatellitePassesApi(api_client)
    pass_prediction = endurosat_api.PassPrediction() # PassPrediction | 

    try:
        # Book a Satellite Pass
        api_response = api_instance.create_satellite_pass(pass_prediction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatellitePassesApi->create_satellite_pass: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_prediction** | [**PassPrediction**](PassPrediction.md)|  | 

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
**201** | Pass booked successfully |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_satellite_passes**
> SatellitePassesResultPage get_filtered_satellite_passes(satellite_id=satellite_id, ground_station=ground_station, status=status, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)

Get Filtered Satellite Passes

This method returns a filtered list of Satellite Passes. Satellite Passes could be filtered by Satellite, Ground Station and Status

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
    api_instance = endurosat_api.SatellitePassesApi(api_client)
    satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the satellite for which to get Satellite Passes (optional)
ground_station = ['gs1'] # list[str] | Specifies the Ground Station(s) of the Satellite Passes to get. (optional)
status = 'status_example' # str | Specifies the Status (or part of the Status) of the Satellite Passes to get (optional)
from_time = 56 # int | Filter to only return entries that were received after the specified time (inclusive) (optional)
to_time = 56 # int | Filter to only return entries that were received before the specified time (exclusive) (optional)
last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)

    try:
        # Get Filtered Satellite Passes
        api_response = api_instance.get_filtered_satellite_passes(satellite_id=satellite_id, ground_station=ground_station, status=status, from_time=from_time, to_time=to_time, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatellitePassesApi->get_filtered_satellite_passes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_id** | **str**| Specifies the satellite for which to get Satellite Passes | [optional] 
 **ground_station** | [**list[str]**](str.md)| Specifies the Ground Station(s) of the Satellite Passes to get. | [optional] 
 **status** | **str**| Specifies the Status (or part of the Status) of the Satellite Passes to get | [optional] 
 **from_time** | **int**| Filter to only return entries that were received after the specified time (inclusive) | [optional] 
 **to_time** | **int**| Filter to only return entries that were received before the specified time (exclusive) | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 

### Return type

[**SatellitePassesResultPage**](SatellitePassesResultPage.md)

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

# **get_satellite_pass_by_id**
> SatellitePass get_satellite_pass_by_id(satellite_pass_id)

Get a Satellite Pass by ID

This method returns a pass by ID for the current user

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
    api_instance = endurosat_api.SatellitePassesApi(api_client)
    satellite_pass_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Pass to get

    try:
        # Get a Satellite Pass by ID
        api_response = api_instance.get_satellite_pass_by_id(satellite_pass_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatellitePassesApi->get_satellite_pass_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_pass_id** | **str**| ID of the Satellite Pass to get | 

### Return type

[**SatellitePass**](SatellitePass.md)

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

# **record_satellite_pass_artifact**
> record_satellite_pass_artifact(satellite_pass_id, artifact_type, payload)

Record a Satellite Pass Artifact

This method records artifacts of the satellite pass

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
    api_instance = endurosat_api.SatellitePassesApi(api_client)
    satellite_pass_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Pass to update
artifact_type = endurosat_api.ArtifactType() # ArtifactType | Specifies the artifact type of the Satellite Passes to upload
payload = '/path/to/file' # file | 

    try:
        # Record a Satellite Pass Artifact
        api_instance.record_satellite_pass_artifact(satellite_pass_id, artifact_type, payload)
    except ApiException as e:
        print("Exception when calling SatellitePassesApi->record_satellite_pass_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_pass_id** | **str**| ID of the Satellite Pass to update | 
 **artifact_type** | [**ArtifactType**](.md)| Specifies the artifact type of the Satellite Passes to upload | 
 **payload** | **file**|  | 

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
**201** | Pass artifact recorded successfully |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**404** | Not Found - A requested resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_satellite_pass_log**
> record_satellite_pass_log(satellite_pass_id, payload)

Record a Satellite Pass Log

This method records a log of the satellite pass

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
    api_instance = endurosat_api.SatellitePassesApi(api_client)
    satellite_pass_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Pass to update
payload = '/path/to/file' # file | 

    try:
        # Record a Satellite Pass Log
        api_instance.record_satellite_pass_log(satellite_pass_id, payload)
    except ApiException as e:
        print("Exception when calling SatellitePassesApi->record_satellite_pass_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_pass_id** | **str**| ID of the Satellite Pass to update | 
 **payload** | **file**|  | 

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
**201** | Pass Log recorded successfully |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**404** | Not Found - A requested resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_satellite_pass_by_id**
> update_satellite_pass_by_id(satellite_pass_id, satellite_pass)

Update a Satellite Pass

This method updates a satellite pass by ID for the current user

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
    api_instance = endurosat_api.SatellitePassesApi(api_client)
    satellite_pass_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Satellite Pass to update
satellite_pass = endurosat_api.SatellitePass() # SatellitePass | 

    try:
        # Update a Satellite Pass
        api_instance.update_satellite_pass_by_id(satellite_pass_id, satellite_pass)
    except ApiException as e:
        print("Exception when calling SatellitePassesApi->update_satellite_pass_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_pass_id** | **str**| ID of the Satellite Pass to update | 
 **satellite_pass** | [**SatellitePass**](SatellitePass.md)|  | 

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

