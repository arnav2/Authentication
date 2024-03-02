# .DefaultApi

All URIs are relative to *https://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authDeleteDelete**](DefaultApi.md#authDeleteDelete) | **DELETE** /auth/delete | Delete User
[**authLoginPost**](DefaultApi.md#authLoginPost) | **POST** /auth/login | Authenticate User
[**authRegisterPost**](DefaultApi.md#authRegisterPost) | **POST** /auth/register | Register User


# **authDeleteDelete**
> void authDeleteDelete()

Deletes the user account.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .DefaultApi(configuration);

let body:any = {};

apiInstance.authDeleteDelete(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters
This endpoint does not need any parameter.


### Return type

**void**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **authLoginPost**
> AuthLoginPost200Response authLoginPost(authLoginPostRequest)

Validates user credentials and returns an access token if successful.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .DefaultApi(configuration);

let body:.DefaultApiAuthLoginPostRequest = {
  // AuthLoginPostRequest
  authLoginPostRequest: {
    email: "user@example.com",
    password: "password123",
  },
};

apiInstance.authLoginPost(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authLoginPostRequest** | **AuthLoginPostRequest**|  |


### Return type

**AuthLoginPost200Response**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **authRegisterPost**
> void authRegisterPost(authLoginPostRequest)

Creates a new user account.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .DefaultApi(configuration);

let body:.DefaultApiAuthRegisterPostRequest = {
  // AuthLoginPostRequest
  authLoginPostRequest: {
    email: "user@example.com",
    password: "password123",
  },
};

apiInstance.authRegisterPost(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authLoginPostRequest** | **AuthLoginPostRequest**|  |


### Return type

**void**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)


