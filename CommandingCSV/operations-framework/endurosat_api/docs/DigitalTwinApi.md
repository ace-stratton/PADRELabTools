# endurosat_api.DigitalTwinApi

All URIs are relative to *https://api.ground-station.endurosat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_simulations**](DigitalTwinApi.md#retrieve_all_simulations) | **GET** /digital-twin/simulations | Returns all simulations
[**retrieve_simulation_output_files**](DigitalTwinApi.md#retrieve_simulation_output_files) | **GET** /digital-twin/simulations/{simulationId} | Returns the simulation details including the output files of the simulation
[**retrieve_simulation_result_files**](DigitalTwinApi.md#retrieve_simulation_result_files) | **GET** /digital-twin/simulations/{simulationId}/result-files | Returns the simulation result files details
[**start_simulation**](DigitalTwinApi.md#start_simulation) | **POST** /digital-twin/simulations | Run simulation for a scheduled telecommand


# **retrieve_all_simulations**
> SimulaitonResultPage retrieve_all_simulations(last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)

Returns all simulations

This method returns all simulations

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
    api_instance = endurosat_api.DigitalTwinApi(api_client)
    last_evaluated_item = '20ec20b5-8535-4593-be85-6fee2a4dd4ba' # str | Specified the ID of the last item that was returned from the last page (optional)
page_size_limit = 56 # int | Specifies the maximum number of results per page. Defaults to 100 (optional)

    try:
        # Returns all simulations
        api_response = api_instance.retrieve_all_simulations(last_evaluated_item=last_evaluated_item, page_size_limit=page_size_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalTwinApi->retrieve_all_simulations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_evaluated_item** | **str**| Specified the ID of the last item that was returned from the last page | [optional] 
 **page_size_limit** | **int**| Specifies the maximum number of results per page. Defaults to 100 | [optional] 

### Return type

[**SimulaitonResultPage**](SimulaitonResultPage.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**200** | All simulations |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_simulation_output_files**
> Simulation retrieve_simulation_output_files(simulation_id)

Returns the simulation details including the output files of the simulation

This method returns the simulation details including the output files of the simulation

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
    api_instance = endurosat_api.DigitalTwinApi(api_client)
    simulation_id = 'simulation_id_example' # str | 

    try:
        # Returns the simulation details including the output files of the simulation
        api_response = api_instance.retrieve_simulation_output_files(simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalTwinApi->retrieve_simulation_output_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 

### Return type

[**Simulation**](Simulation.md)

### Authorization

[MyEnduroSat](../README.md#MyEnduroSat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Received a malformed or invalid request |  -  |
**200** | Simulation details |  -  |
**401** | Unauthenticated - No authentication token provided |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_simulation_result_files**
> SimulationResultFilesDetails retrieve_simulation_result_files(simulation_id)

Returns the simulation result files details

This method returns the simulation result files details including download url

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
    api_instance = endurosat_api.DigitalTwinApi(api_client)
    simulation_id = 'simulation_id_example' # str | 

    try:
        # Returns the simulation result files details
        api_response = api_instance.retrieve_simulation_result_files(simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalTwinApi->retrieve_simulation_result_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 

### Return type

[**SimulationResultFilesDetails**](SimulationResultFilesDetails.md)

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
**200** | Simulation result files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_simulation**
> str start_simulation(simulation_request)

Run simulation for a scheduled telecommand

This method runs simulation for a scheduled telecommand

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
    api_instance = endurosat_api.DigitalTwinApi(api_client)
    simulation_request = endurosat_api.SimulationRequest() # SimulationRequest | 

    try:
        # Run simulation for a scheduled telecommand
        api_response = api_instance.start_simulation(simulation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalTwinApi->start_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_request** | [**SimulationRequest**](SimulationRequest.md)|  | 

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
**201** | Simulation started |  -  |
**403** | Unauthorized - User has insufficient privileges. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

