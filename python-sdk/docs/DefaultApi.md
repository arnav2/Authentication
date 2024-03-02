# openapi_client.DefaultApi

All URIs are relative to *https://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_delete_delete**](DefaultApi.md#auth_delete_delete) | **DELETE** /auth/delete | Delete User
[**auth_login_post**](DefaultApi.md#auth_login_post) | **POST** /auth/login | Authenticate User
[**auth_register_post**](DefaultApi.md#auth_register_post) | **POST** /auth/register | Register User


# **auth_delete_delete**
> auth_delete_delete()

Delete User

Deletes the user account.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Delete User
        api_instance.auth_delete_delete()
    except Exception as e:
        print("Exception when calling DefaultApi->auth_delete_delete: %s\n" % e)
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
**204** | User deleted successfully |  -  |
**401** | Unauthorized - Missing or invalid token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_post**
> AuthLoginPost200Response auth_login_post(auth_login_post_request)

Authenticate User

Validates user credentials and returns an access token if successful.

### Example


```python
import openapi_client
from openapi_client.models.auth_login_post200_response import AuthLoginPost200Response
from openapi_client.models.auth_login_post_request import AuthLoginPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    auth_login_post_request = openapi_client.AuthLoginPostRequest() # AuthLoginPostRequest | 

    try:
        # Authenticate User
        api_response = api_instance.auth_login_post(auth_login_post_request)
        print("The response of DefaultApi->auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_post_request** | [**AuthLoginPostRequest**](AuthLoginPostRequest.md)|  | 

### Return type

[**AuthLoginPost200Response**](AuthLoginPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful authentication |  -  |
**401** | Unauthorized - Invalid credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_register_post**
> auth_register_post(auth_login_post_request)

Register User

Creates a new user account.

### Example


```python
import openapi_client
from openapi_client.models.auth_login_post_request import AuthLoginPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    auth_login_post_request = openapi_client.AuthLoginPostRequest() # AuthLoginPostRequest | 

    try:
        # Register User
        api_instance.auth_register_post(auth_login_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_register_post: %s\n" % e)
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
**201** | User created successfully |  -  |
**400** | Bad request - Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

