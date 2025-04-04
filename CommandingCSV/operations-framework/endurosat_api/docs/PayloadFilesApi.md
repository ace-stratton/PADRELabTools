# endurosat_api.PayloadFilesApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finish_multipart_upload**](PayloadFilesApi.md#finish_multipart_upload) | **PUT** /payload-files/finish | Finish multipart upload
[**get_download_url**](PayloadFilesApi.md#get_download_url) | **GET** /payload-files/{resourceType}/{resourceId} | (DEPRECATED) Get a URL from which to download a file. Use GET /{resourceType}/{resourceId}/artifacts/{artifactType} instead.
[**get_download_url1**](PayloadFilesApi.md#get_download_url1) | **GET** /payload-files/{resourceType}/{resourceId}/artifacts/{artifactType} | Get a URL from which to download a file
[**initiate_multipart_upload**](PayloadFilesApi.md#initiate_multipart_upload) | **POST** /payload-files/multipart/{resourceType}/{resourceId} | Initiate Multipart Upload
[**upload_artifact_file**](PayloadFilesApi.md#upload_artifact_file) | **PUT** /payload-files/{resourceType}/{resourceId}/artifacts/{artifactType} | Attach payload file to resouce
[**upload_file**](PayloadFilesApi.md#upload_file) | **PUT** /payload-files/{resourceType}/{resourceId} | (DEPRECATED) Attach payload file to resouce. Use PUT /{resourceType}/{resourceId}/artifacts/{artifactType} instead.
[**upload_part**](PayloadFilesApi.md#upload_part) | **PUT** /payload-files/upload-part | Upload Part


# **finish_multipart_upload**
> object finish_multipart_upload(multipart_upload_id, e_tags)

Finish multipart upload

This method finishes a multipart upload

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
    api_instance = endurosat_api.PayloadFilesApi(api_client)
    multipart_upload_id = 'multipart_upload_id_example' # str | 
e_tags = ['e_tags_example'] # list[str] | 

    try:
        # Finish multipart upload
        api_response = api_instance.finish_multipart_upload(multipart_upload_id, e_tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadFilesApi->finish_multipart_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multipart_upload_id** | **str**|  | 
 **e_tags** | [**list[str]**](str.md)|  | 

### Return type

**object**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_url**
> str get_download_url(resource_type, resource_id)

(DEPRECATED) Get a URL from which to download a file. Use GET /{resourceType}/{resourceId}/artifacts/{artifactType} instead.

This method returns a URL from which to download a file

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
    api_instance = endurosat_api.PayloadFilesApi(api_client)
    resource_type = 'telemetry' # str | Type of the resource for which to get a file. Possible values are 'telemetry', 'telecommand' and 'satellite-pass'.
resource_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Id of the resource for which to get a file

    try:
        # (DEPRECATED) Get a URL from which to download a file. Use GET /{resourceType}/{resourceId}/artifacts/{artifactType} instead.
        api_response = api_instance.get_download_url(resource_type, resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadFilesApi->get_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of the resource for which to get a file. Possible values are &#39;telemetry&#39;, &#39;telecommand&#39; and &#39;satellite-pass&#39;. | 
 **resource_id** | **str**| Id of the resource for which to get a file | 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_url1**
> str get_download_url1(resource_type, resource_id, artifact_type)

Get a URL from which to download a file

This method returns a URL from which to download a file

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
    api_instance = endurosat_api.PayloadFilesApi(api_client)
    resource_type = 'telemetry' # str | Type of the resource for which to get a file. Possible values are 'telemetry', 'telecommand' and 'satellite-pass'.
resource_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Id of the resource for which to get a file
artifact_type = endurosat_api.ArtifactType() # ArtifactType | Specifies the artifact type of the Satellite Passes to get

    try:
        # Get a URL from which to download a file
        api_response = api_instance.get_download_url1(resource_type, resource_id, artifact_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadFilesApi->get_download_url1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of the resource for which to get a file. Possible values are &#39;telemetry&#39;, &#39;telecommand&#39; and &#39;satellite-pass&#39;. | 
 **resource_id** | **str**| Id of the resource for which to get a file | 
 **artifact_type** | [**ArtifactType**](.md)| Specifies the artifact type of the Satellite Passes to get | 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_multipart_upload**
> str initiate_multipart_upload(resource_type, resource_id)

Initiate Multipart Upload

This method begins a multipart upload

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
    api_instance = endurosat_api.PayloadFilesApi(api_client)
    resource_type = 'telemetry' # str | Type of the resource for which to init a file upload. Possible values are 'telemetry', 'telecommand' and 'satellite-pass'.
resource_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Id of the resource for which to init a file upload

    try:
        # Initiate Multipart Upload
        api_response = api_instance.initiate_multipart_upload(resource_type, resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadFilesApi->initiate_multipart_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of the resource for which to init a file upload. Possible values are &#39;telemetry&#39;, &#39;telecommand&#39; and &#39;satellite-pass&#39;. | 
 **resource_id** | **str**| Id of the resource for which to init a file upload | 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_artifact_file**
> upload_artifact_file(resource_type, resource_id, artifact_type, payload)

Attach payload file to resouce

This method attaches a payload file to a resouce

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
    api_instance = endurosat_api.PayloadFilesApi(api_client)
    resource_type = 'telemetry' # str | Type of the resource for which to upload a file. Possible values are 'telemetry', 'telecommand' and 'satellite-pass'.
resource_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Id of the resource for which to upload a file
artifact_type = endurosat_api.ArtifactType() # ArtifactType | Specifies the artifact type of the Satellite Passes to upload
payload = '/path/to/file' # file | 

    try:
        # Attach payload file to resouce
        api_instance.upload_artifact_file(resource_type, resource_id, artifact_type, payload)
    except ApiException as e:
        print("Exception when calling PayloadFilesApi->upload_artifact_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of the resource for which to upload a file. Possible values are &#39;telemetry&#39;, &#39;telecommand&#39; and &#39;satellite-pass&#39;. | 
 **resource_id** | **str**| Id of the resource for which to upload a file | 
 **artifact_type** | [**ArtifactType**](.md)| Specifies the artifact type of the Satellite Passes to upload | 
 **payload** | **file**|  | 

### Return type

void (empty response body)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> upload_file(resource_type, resource_id, payload)

(DEPRECATED) Attach payload file to resouce. Use PUT /{resourceType}/{resourceId}/artifacts/{artifactType} instead.

This method attaches a payload file to a resouce

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
    api_instance = endurosat_api.PayloadFilesApi(api_client)
    resource_type = 'telemetry' # str | Type of the resource for which to upload a file. Possible values are 'telemetry', 'telecommand' and 'satellite-pass'.
resource_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Id of the resource for which to upload a file
payload = '/path/to/file' # file | 

    try:
        # (DEPRECATED) Attach payload file to resouce. Use PUT /{resourceType}/{resourceId}/artifacts/{artifactType} instead.
        api_instance.upload_file(resource_type, resource_id, payload)
    except ApiException as e:
        print("Exception when calling PayloadFilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of the resource for which to upload a file. Possible values are &#39;telemetry&#39;, &#39;telecommand&#39; and &#39;satellite-pass&#39;. | 
 **resource_id** | **str**| Id of the resource for which to upload a file | 
 **payload** | **file**|  | 

### Return type

void (empty response body)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_part**
> str upload_part(multipart_upload_id, part_number, payload, last_part=last_part)

Upload Part

This method uploads a part of a multipart file upload

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
    api_instance = endurosat_api.PayloadFilesApi(api_client)
    multipart_upload_id = 'multipart_upload_id_example' # str | 
part_number = 56 # int | 
payload = '/path/to/file' # file | 
last_part = True # bool |  (optional)

    try:
        # Upload Part
        api_response = api_instance.upload_part(multipart_upload_id, part_number, payload, last_part=last_part)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadFilesApi->upload_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multipart_upload_id** | **str**|  | 
 **part_number** | **int**|  | 
 **payload** | **file**|  | 
 **last_part** | **bool**|  | [optional] 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

