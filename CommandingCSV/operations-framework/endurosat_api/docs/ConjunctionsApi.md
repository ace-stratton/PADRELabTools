# endurosat_api.ConjunctionsApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filtered_conjunctions**](ConjunctionsApi.md#get_filtered_conjunctions) | **GET** /ca/conjunctions | Get Conjunctions


# **get_filtered_conjunctions**
> ConjunctionEvent get_filtered_conjunctions(conjunction_id=conjunction_id, satellite_id=satellite_id, start_date=start_date, end_date=end_date, collision_probability=collision_probability, page=page, per_page=per_page)

Get Conjunctions

This method returns a filtered list of conjunctions

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
    api_instance = endurosat_api.ConjunctionsApi(api_client)
    conjunction_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Conjunction (optional)
satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the satellite for which to get the conjunction (optional)
start_date = '1613865691000' # str | Start date for which to get the conjunction (optional)
end_date = '1613865691000' # str | End date for which to get the conjunction (optional)
collision_probability = '98213098213' # str | The probability of the conjunction (optional)
page = '4' # str | Number of the page (optional)
per_page = '100' # str | Number of items per page (optional)

    try:
        # Get Conjunctions
        api_response = api_instance.get_filtered_conjunctions(conjunction_id=conjunction_id, satellite_id=satellite_id, start_date=start_date, end_date=end_date, collision_probability=collision_probability, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConjunctionsApi->get_filtered_conjunctions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conjunction_id** | **str**| ID of the Conjunction | [optional] 
 **satellite_id** | **str**| ID of the satellite for which to get the conjunction | [optional] 
 **start_date** | **str**| Start date for which to get the conjunction | [optional] 
 **end_date** | **str**| End date for which to get the conjunction | [optional] 
 **collision_probability** | **str**| The probability of the conjunction | [optional] 
 **page** | **str**| Number of the page | [optional] 
 **per_page** | **str**| Number of items per page | [optional] 

### Return type

[**ConjunctionEvent**](ConjunctionEvent.md)

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

