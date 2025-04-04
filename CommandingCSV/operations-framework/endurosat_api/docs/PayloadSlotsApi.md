# endurosat_api.PayloadSlotsApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payload_slot**](PayloadSlotsApi.md#create_payload_slot) | **POST** /payload-slots | Create a Payload Slot
[**get_payload_slot_by_id**](PayloadSlotsApi.md#get_payload_slot_by_id) | **GET** /payload-slots/{payloadSlotId} | Get a Payload Slot by ID
[**get_payload_slots**](PayloadSlotsApi.md#get_payload_slots) | **GET** /payload-slots | Get a list of available Payload Slots


# **create_payload_slot**
> str create_payload_slot(payload_slot)

Create a Payload Slot

This method creates a new Payload Slot for the current user.

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
    api_instance = endurosat_api.PayloadSlotsApi(api_client)
    payload_slot = endurosat_api.PayloadSlot() # PayloadSlot | 

    try:
        # Create a Payload Slot
        api_response = api_instance.create_payload_slot(payload_slot)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadSlotsApi->create_payload_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_slot** | [**PayloadSlot**](PayloadSlot.md)|  | 

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
**201** | Payload Slot created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payload_slot_by_id**
> PayloadSlot get_payload_slot_by_id(payload_slot_id)

Get a Payload Slot by ID

This method returns a Payload Slot by ID

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
    api_instance = endurosat_api.PayloadSlotsApi(api_client)
    payload_slot_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Payload Slot to get.

    try:
        # Get a Payload Slot by ID
        api_response = api_instance.get_payload_slot_by_id(payload_slot_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadSlotsApi->get_payload_slot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_slot_id** | **str**| ID of the Payload Slot to get. | 

### Return type

[**PayloadSlot**](PayloadSlot.md)

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

# **get_payload_slots**
> list[PayloadSlot] get_payload_slots(satellite_subsystem)

Get a list of available Payload Slots

This method returns a list of available Payload Slots for a payload satellite subsytem

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
    api_instance = endurosat_api.PayloadSlotsApi(api_client)
    satellite_subsystem = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the satellite subsystem (payload) to get slots for.

    try:
        # Get a list of available Payload Slots
        api_response = api_instance.get_payload_slots(satellite_subsystem)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadSlotsApi->get_payload_slots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_subsystem** | **str**| ID of the satellite subsystem (payload) to get slots for. | 

### Return type

[**list[PayloadSlot]**](PayloadSlot.md)

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

