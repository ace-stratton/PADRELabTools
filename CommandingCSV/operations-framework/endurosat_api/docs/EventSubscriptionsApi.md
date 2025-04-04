# endurosat_api.EventSubscriptionsApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_subscription**](EventSubscriptionsApi.md#create_event_subscription) | **POST** /event-subscriptions | Create an event subscription
[**get_filtered_event_subscriptions**](EventSubscriptionsApi.md#get_filtered_event_subscriptions) | **GET** /event-subscriptions | Get event subscription by event type


# **create_event_subscription**
> str create_event_subscription(create_event_subscription_request)

Create an event subscription

This method creates an event subscription

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
    api_instance = endurosat_api.EventSubscriptionsApi(api_client)
    create_event_subscription_request = endurosat_api.CreateEventSubscriptionRequest() # CreateEventSubscriptionRequest | 

    try:
        # Create an event subscription
        api_response = api_instance.create_event_subscription(create_event_subscription_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventSubscriptionsApi->create_event_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_subscription_request** | [**CreateEventSubscriptionRequest**](CreateEventSubscriptionRequest.md)|  | 

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
**403** | Unauthorized - User has insufficient privileges. |  -  |
**201** | Created Event Subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_event_subscriptions**
> EventSubscriptionsResultPage get_filtered_event_subscriptions(event_type=event_type, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)

Get event subscription by event type

This method returns an event subscription by event type

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
    api_instance = endurosat_api.EventSubscriptionsApi(api_client)
    event_type = 'event_type_example' # str | Event Type (optional)
last_evaluated_item = 'last_evaluated_item_example' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)

    try:
        # Get event subscription by event type
        api_response = api_instance.get_filtered_event_subscriptions(event_type=event_type, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventSubscriptionsApi->get_filtered_event_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| Event Type | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 

### Return type

[**EventSubscriptionsResultPage**](EventSubscriptionsResultPage.md)

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

