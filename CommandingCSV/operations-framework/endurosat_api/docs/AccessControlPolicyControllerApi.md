# endurosat_api.AccessControlPolicyControllerApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](AccessControlPolicyControllerApi.md#delete) | **DELETE** /access-control-policies/{name} | 
[**get_all**](AccessControlPolicyControllerApi.md#get_all) | **GET** /access-control-policies | 
[**get_by_name**](AccessControlPolicyControllerApi.md#get_by_name) | **GET** /access-control-policies/{name} | 
[**save**](AccessControlPolicyControllerApi.md#save) | **POST** /access-control-policies | 
[**update**](AccessControlPolicyControllerApi.md#update) | **PUT** /access-control-policies | 


# **delete**
> delete(name)



### Example

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


# Enter a context with an instance of the API client
with endurosat_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.AccessControlPolicyControllerApi(api_client)
    name = 'name_example' # str | 

    try:
        api_instance.delete(name)
    except ApiException as e:
        print("Exception when calling AccessControlPolicyControllerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> list[CombinedAccessControlPolicy] get_all()



### Example

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


# Enter a context with an instance of the API client
with endurosat_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.AccessControlPolicyControllerApi(api_client)
    
    try:
        api_response = api_instance.get_all()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessControlPolicyControllerApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CombinedAccessControlPolicy]**](CombinedAccessControlPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name**
> CombinedAccessControlPolicy get_by_name(name)



### Example

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


# Enter a context with an instance of the API client
with endurosat_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.AccessControlPolicyControllerApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.get_by_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessControlPolicyControllerApi->get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**CombinedAccessControlPolicy**](CombinedAccessControlPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> CombinedAccessControlPolicy save(combined_access_control_policy_request_dto)



### Example

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


# Enter a context with an instance of the API client
with endurosat_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.AccessControlPolicyControllerApi(api_client)
    combined_access_control_policy_request_dto = endurosat_api.CombinedAccessControlPolicyRequestDTO() # CombinedAccessControlPolicyRequestDTO | 

    try:
        api_response = api_instance.save(combined_access_control_policy_request_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessControlPolicyControllerApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_access_control_policy_request_dto** | [**CombinedAccessControlPolicyRequestDTO**](CombinedAccessControlPolicyRequestDTO.md)|  | 

### Return type

[**CombinedAccessControlPolicy**](CombinedAccessControlPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> CombinedAccessControlPolicy update(combined_access_control_policy_request_dto)



### Example

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


# Enter a context with an instance of the API client
with endurosat_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endurosat_api.AccessControlPolicyControllerApi(api_client)
    combined_access_control_policy_request_dto = endurosat_api.CombinedAccessControlPolicyRequestDTO() # CombinedAccessControlPolicyRequestDTO | 

    try:
        api_response = api_instance.update(combined_access_control_policy_request_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessControlPolicyControllerApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_access_control_policy_request_dto** | [**CombinedAccessControlPolicyRequestDTO**](CombinedAccessControlPolicyRequestDTO.md)|  | 

### Return type

[**CombinedAccessControlPolicy**](CombinedAccessControlPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

