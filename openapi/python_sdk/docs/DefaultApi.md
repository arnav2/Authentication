# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hello_get**](DefaultApi.md#hello_get) | **GET** /hello | Get Hello Message


# **hello_get**
> HelloGet200Response hello_get()

Get Hello Message

Returns a simple hello message

### Example


```python
import openapi_client
from openapi_client.models.hello_get200_response import HelloGet200Response
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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Hello Message
        api_response = api_instance.hello_get()
        print("The response of DefaultApi->hello_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hello_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HelloGet200Response**](HelloGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

