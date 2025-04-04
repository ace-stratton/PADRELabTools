# endurosat_api.MissionDatabasesApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mission_database**](MissionDatabasesApi.md#create_mission_database) | **POST** /mission-databases | Create a Mission Database
[**create_mission_database_package**](MissionDatabasesApi.md#create_mission_database_package) | **POST** /mission-databases/fidl-packages | Generate fidl parsers and mission databases from deployment model
[**create_procedure_scripts**](MissionDatabasesApi.md#create_procedure_scripts) | **POST** /mission-databases/{missionDatabaseId}/procedure-scripts | Upload mission database operation script
[**delete_mission_database**](MissionDatabasesApi.md#delete_mission_database) | **DELETE** /mission-databases/{missionDatabaseId} | Delete a MissionDatabase by ID
[**delete_mission_database_package**](MissionDatabasesApi.md#delete_mission_database_package) | **DELETE** /mission-databases/fidl-packages/{packageId} | Delete all files and mission databases for package
[**delete_procedure_scripts**](MissionDatabasesApi.md#delete_procedure_scripts) | **DELETE** /mission-databases/{missionDatabaseId}/procedure-scripts/{procedureName} | Delete a script for this mission database
[**get_filtered_mission_database**](MissionDatabasesApi.md#get_filtered_mission_database) | **GET** /mission-databases | Get Mission Databases
[**get_mission_database_by_id**](MissionDatabasesApi.md#get_mission_database_by_id) | **GET** /mission-databases/{missionDatabaseId} | Get Mission Database By ID
[**get_mission_database_definition**](MissionDatabasesApi.md#get_mission_database_definition) | **GET** /mission-databases/{missionDatabaseId}/definition | Get Mission Database Definition by Mission Database ID
[**get_mission_database_packag_by_id**](MissionDatabasesApi.md#get_mission_database_packag_by_id) | **GET** /mission-databases/fidl-packages/{packageId} | Get mission database package
[**get_mission_database_package_source_by_id**](MissionDatabasesApi.md#get_mission_database_package_source_by_id) | **GET** /mission-databases/fidl-packages/{packageId}/source | Get fidl package source
[**get_mission_database_parser**](MissionDatabasesApi.md#get_mission_database_parser) | **GET** /mission-databases/{missionDatabaseId}/parser | Get URL from which to download Mission Database Fidl Parser by Mission Database ID
[**get_mission_database_procedure_script**](MissionDatabasesApi.md#get_mission_database_procedure_script) | **GET** /mission-databases/{missionDatabaseId}/procedure/{procedureName} | Get Mission Database Procedure by Mission Database ID and Procedure Name
[**update_mission_database**](MissionDatabasesApi.md#update_mission_database) | **PUT** /mission-databases/{missionDatabaseId} | Update a MissionDatabase


# **create_mission_database**
> str create_mission_database(mission_database)

Create a Mission Database

This method creates new mission database.

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database = endurosat_api.MissionDatabase() # MissionDatabase | 

    try:
        # Create a Mission Database
        api_response = api_instance.create_mission_database(mission_database)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->create_mission_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database** | [**MissionDatabase**](MissionDatabase.md)|  | 

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
**201** | Mission Database created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mission_database_package**
> str create_mission_database_package(fidl_package, deployment_model=deployment_model)

Generate fidl parsers and mission databases from deployment model

This method generates new parsers and mission databases based on deploy model.

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    fidl_package = '/path/to/file' # file | The archive containing the fidl files and deployment model
deployment_model = 'deployment_model_example' # str | Name of .fdepl deployment model file (excluding the .fdepl extension) (optional)

    try:
        # Generate fidl parsers and mission databases from deployment model
        api_response = api_instance.create_mission_database_package(fidl_package, deployment_model=deployment_model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->create_mission_database_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fidl_package** | **file**| The archive containing the fidl files and deployment model | 
 **deployment_model** | **str**| Name of .fdepl deployment model file (excluding the .fdepl extension) | [optional] 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**201** | Parser created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_procedure_scripts**
> str create_procedure_scripts(mission_database_id, procedure_description, procedure_name, procedure_scripts)

Upload mission database operation script

This method will upload .

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Mission Database
procedure_description = 'procedure_description_example' # str | Short explanation what is the script expected to do
procedure_name = 'procedure_name_example' # str | Short explanation what is the script expected to do
procedure_scripts = '/path/to/file' # file | The archive containing the operation scripts

    try:
        # Upload mission database operation script
        api_response = api_instance.create_procedure_scripts(mission_database_id, procedure_description, procedure_name, procedure_scripts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->create_procedure_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the Mission Database | 
 **procedure_description** | **str**| Short explanation what is the script expected to do | 
 **procedure_name** | **str**| Short explanation what is the script expected to do | 
 **procedure_scripts** | **file**| The archive containing the operation scripts | 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**201** | Procedure script uploaded successfully |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mission_database**
> delete_mission_database(mission_database_id)

Delete a MissionDatabase by ID

This method deletes a MissionDatabase with the specified ID

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the MissionDatabase to delete

    try:
        # Delete a MissionDatabase by ID
        api_instance.delete_mission_database(mission_database_id)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->delete_mission_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the MissionDatabase to delete | 

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

# **delete_mission_database_package**
> delete_mission_database_package(package_id)

Delete all files and mission databases for package

This method deletes a Mission Database Package with the specified ID along with all associated mission databases and files

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    package_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Mission Database Package to delete

    try:
        # Delete all files and mission databases for package
        api_instance.delete_mission_database_package(package_id)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->delete_mission_database_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**| ID of the Mission Database Package to delete | 

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

# **delete_procedure_scripts**
> delete_procedure_scripts(mission_database_id, procedure_name)

Delete a script for this mission database

This method deletes a Mission Database Package with the specified ID along with all associated mission databases and files

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Mission Database
procedure_name = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Name of the procedure script that will be deleted

    try:
        # Delete a script for this mission database
        api_instance.delete_procedure_scripts(mission_database_id, procedure_name)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->delete_procedure_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the Mission Database | 
 **procedure_name** | **str**| Name of the procedure script that will be deleted | 

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

# **get_filtered_mission_database**
> MissionDatabasesResultPage get_filtered_mission_database(satellite_id=satellite_id, satellite_subsystem_id=satellite_subsystem_id, name=name, type=type, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)

Get Mission Databases

This method returns a filtered list of Mission Databases for a satellite. Mission Databases could be filtered by Satellite, Satellite Subsytem, name and type

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    satellite_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the Satellite for which the Mission Database is applicable (optional)
satellite_subsystem_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specifies the Satellite Subsystem for which the Mission Database is applicable (optional)
name = 'beacons' # str | Specifies the name of the Mission Database (optional)
type = 'fidl' # str | Specifies the type of the Mission Database (optional)
last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)

    try:
        # Get Mission Databases
        api_response = api_instance.get_filtered_mission_database(satellite_id=satellite_id, satellite_subsystem_id=satellite_subsystem_id, name=name, type=type, last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->get_filtered_mission_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **satellite_id** | **str**| Specifies the Satellite for which the Mission Database is applicable | [optional] 
 **satellite_subsystem_id** | **str**| Specifies the Satellite Subsystem for which the Mission Database is applicable | [optional] 
 **name** | **str**| Specifies the name of the Mission Database | [optional] 
 **type** | **str**| Specifies the type of the Mission Database | [optional] 
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 

### Return type

[**MissionDatabasesResultPage**](MissionDatabasesResultPage.md)

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

# **get_mission_database_by_id**
> MissionDatabase get_mission_database_by_id(mission_database_id)

Get Mission Database By ID

This method returns a Mission Database by ID.

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Mission Database to get

    try:
        # Get Mission Database By ID
        api_response = api_instance.get_mission_database_by_id(mission_database_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->get_mission_database_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the Mission Database to get | 

### Return type

[**MissionDatabase**](MissionDatabase.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mission_database_definition**
> str get_mission_database_definition(mission_database_id)

Get Mission Database Definition by Mission Database ID

This method returns a Mission Database Definition based on the ID of a Mission Database for the current user

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Mission Database for which to get the Definition

    try:
        # Get Mission Database Definition by Mission Database ID
        api_response = api_instance.get_mission_database_definition(mission_database_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->get_mission_database_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the Mission Database for which to get the Definition | 

### Return type

**str**

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

# **get_mission_database_packag_by_id**
> MissionDatabasePackage get_mission_database_packag_by_id(package_id)

Get mission database package

This method returns a mission database package by Id.

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    package_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the package generated from the fidl source

    try:
        # Get mission database package
        api_response = api_instance.get_mission_database_packag_by_id(package_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->get_mission_database_packag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**| ID of the package generated from the fidl source | 

### Return type

[**MissionDatabasePackage**](MissionDatabasePackage.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**200** | Mission Database Package returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mission_database_package_source_by_id**
> get_mission_database_package_source_by_id(package_id)

Get fidl package source

This method returns a url to download the archive with fidl files used for the generation of the package.

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    package_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the package generated from the fidl source

    try:
        # Get fidl package source
        api_instance.get_mission_database_package_source_by_id(package_id)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->get_mission_database_package_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**| ID of the package generated from the fidl source | 

### Return type

void (empty response body)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**200** | Source archive returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mission_database_parser**
> str get_mission_database_parser(mission_database_id)

Get URL from which to download Mission Database Fidl Parser by Mission Database ID

This method returns a URL from which to download Mission Database Parser based on the ID of a Mission Database for the current user

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Mission Database for which to get the URL

    try:
        # Get URL from which to download Mission Database Fidl Parser by Mission Database ID
        api_response = api_instance.get_mission_database_parser(mission_database_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->get_mission_database_parser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the Mission Database for which to get the URL | 

### Return type

**str**

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**200** | URL to download the Mission Database Parser |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |
**404** | Not Found - A requested resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mission_database_procedure_script**
> str get_mission_database_procedure_script(mission_database_id, procedure_name)

Get Mission Database Procedure by Mission Database ID and Procedure Name

This method returns a Mission Database Procedure based on the ID of a Mission Database and Procedure Name for the current user

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the Mission Database for which to get the Procedure
procedure_name = 'Spin_Y-wheel-2000' # str | Name of the Procedure

    try:
        # Get Mission Database Procedure by Mission Database ID and Procedure Name
        api_response = api_instance.get_mission_database_procedure_script(mission_database_id, procedure_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->get_mission_database_procedure_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the Mission Database for which to get the Procedure | 
 **procedure_name** | **str**| Name of the Procedure | 

### Return type

**str**

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

# **update_mission_database**
> update_mission_database(mission_database_id, mission_database)

Update a MissionDatabase

This method updates a MissionDatabase by ID

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
    api_instance = endurosat_api.MissionDatabasesApi(api_client)
    mission_database_id = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | ID of the MissionDatabase to update
mission_database = endurosat_api.MissionDatabase() # MissionDatabase | 

    try:
        # Update a MissionDatabase
        api_instance.update_mission_database(mission_database_id, mission_database)
    except ApiException as e:
        print("Exception when calling MissionDatabasesApi->update_mission_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_database_id** | **str**| ID of the MissionDatabase to update | 
 **mission_database** | [**MissionDatabase**](MissionDatabase.md)|  | 

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

