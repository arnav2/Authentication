# openapi_client.DefaultApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](DefaultApi.md#auth_login_post) | **POST** /auth/login | Authenticate User


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

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
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

