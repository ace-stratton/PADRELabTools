# endurosat_api.SatellitePassPredictionsApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pass_predictions**](SatellitePassPredictionsApi.md#get_pass_predictions) | **GET** /pass-predictions | Get a list of pass predictions


# **get_pass_predictions**
> list[PassPrediction] get_pass_predictions(satellite, ground_station=ground_station, hours_ahead=hours_ahead)

Get a list of pass predictions

This method returns a list of pass predictions that could be filtered by satellite, ground station and time window. These predictions can then be used to schedule a pass. Each prediction is valid for 20 minutes. After that the prediction API need to be called again.

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
    api_instance = endurosat_api.SatellitePassPredictionsApi(api_client)
    satellite = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the satellite for which to filter.
ground_station = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the ground station for which to filter. If not present results for all ground stations are returned. (optional)
hours_ahead = 56 # int | Specified the time window in hours from now for which to predict passes. Defaults to 10. (optional)

    try:
        # Get a list of pass predictions
        api_response = api_instance.get_pass_predictions(satellite, ground_station=ground_station, hours_ahead=hours_ahead)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatellitePassPredictionsApi->get_pass_predictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite** | **str**| ID of the satellite for which to filter. | 
 **ground_station** | **str**| ID of the ground station for which to filter. If not present results for all ground stations are returned. | [optional] 
 **hours_ahead** | **int**| Specified the time window in hours from now for which to predict passes. Defaults to 10. | [optional] 

### Return type

[**list[PassPrediction]**](PassPrediction.md)

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
**404** | Not Found - A requested resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

