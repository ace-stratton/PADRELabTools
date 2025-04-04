# endurosat_api.AuthenticationApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /oauth2/token | Authenticates a user or refresh a token
[**revoke_token**](AuthenticationApi.md#revoke_token) | **POST** /oauth2/revoke | Revoke a refresh a token


# **authenticate**
> AuthenticationResponse authenticate(client_id, grant_type, username=username, password=password, refresh_token=refresh_token)

Authenticates a user or refresh a token

This method authenticates a user or refreshes a token.

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
    api_instance = endurosat_api.AuthenticationApi(api_client)
    client_id = 'client_id_example' # str | App Client ID
grant_type = 'grant_type_example' # str | The oauth2 grant type
username = 'username_example' # str | Username - required for grant_type=password (optional)
password = 'password_example' # str | Password - required for grant_type=password (optional)
refresh_token = 'refresh_token_example' # str | Refresh Token - required for grant_type=refresh_token (optional)

    try:
        # Authenticates a user or refresh a token
        api_response = api_instance.authenticate(client_id, grant_type, username=username, password=password, refresh_token=refresh_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| App Client ID | 
 **grant_type** | **str**| The oauth2 grant type | 
 **username** | **str**| Username - required for grant_type&#x3D;password | [optional] 
 **password** | **str**| Password - required for grant_type&#x3D;password | [optional] 
 **refresh_token** | **str**| Refresh Token - required for grant_type&#x3D;refresh_token | [optional] 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Provided credentials are invalid |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> revoke_token(client_id, token)

Revoke a refresh a token

This method revokes a refreshe token.

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
    api_instance = endurosat_api.AuthenticationApi(api_client)
    client_id = 'client_id_example' # str | App Client ID
token = 'token_example' # str | The token to revoke

    try:
        # Revoke a refresh a token
        api_instance.revoke_token(client_id, token)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->revoke_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| App Client ID | 
 **token** | **str**| The token to revoke | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**204** | No Content - Request was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

