# openapi_client.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_delete_post**](AuthenticationApi.md#auth_delete_post) | **POST** /auth/delete | Delete user endpoint
[**auth_login_post**](AuthenticationApi.md#auth_login_post) | **POST** /auth/login | Login endpoint
[**auth_logout_post**](AuthenticationApi.md#auth_logout_post) | **POST** /auth/logout | Logout endpoint
[**auth_register_post**](AuthenticationApi.md#auth_register_post) | **POST** /auth/register | Register endpoint


# **auth_delete_post**
> auth_delete_post(auth_delete_post_request)

Delete user endpoint

### Example


```python
import openapi_client
from openapi_client.models.auth_delete_post_request import AuthDeletePostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)
    auth_delete_post_request = openapi_client.AuthDeletePostRequest() # AuthDeletePostRequest | 

    try:
        # Delete user endpoint
        api_instance.auth_delete_post(auth_delete_post_request)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_delete_post_request** | [**AuthDeletePostRequest**](AuthDeletePostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User deleted successfully |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_post**
> auth_login_post(auth_login_post_request)

Login endpoint

### Example


```python
import openapi_client
from openapi_client.models.auth_login_post_request import AuthLoginPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)
    auth_login_post_request = openapi_client.AuthLoginPostRequest() # AuthLoginPostRequest | 

    try:
        # Login endpoint
        api_instance.auth_login_post(auth_login_post_request)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_post_request** | [**AuthLoginPostRequest**](AuthLoginPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful login |  -  |
**400** | Bad request, invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout_post**
> auth_logout_post()

Logout endpoint

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)

    try:
        # Logout endpoint
        api_instance.auth_logout_post()
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_logout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful logout |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_register_post**
> auth_register_post(auth_login_post_request)

Register endpoint

### Example


```python
import openapi_client
from openapi_client.models.auth_login_post_request import AuthLoginPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)
    auth_login_post_request = openapi_client.AuthLoginPostRequest() # AuthLoginPostRequest | 

    try:
        # Register endpoint
        api_instance.auth_register_post(auth_login_post_request)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_post_request** | [**AuthLoginPostRequest**](AuthLoginPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User registered successfully |  -  |
**400** | Bad request, invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

