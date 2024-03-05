# .AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authDeletePost**](AuthenticationApi.md#authDeletePost) | **POST** /auth/delete | Delete user endpoint
[**authLoginPost**](AuthenticationApi.md#authLoginPost) | **POST** /auth/login | Login endpoint
[**authLogoutPost**](AuthenticationApi.md#authLogoutPost) | **POST** /auth/logout | Logout endpoint
[**authRegisterPost**](AuthenticationApi.md#authRegisterPost) | **POST** /auth/register | Register endpoint


# **authDeletePost**
> void authDeletePost(authDeletePostRequest)


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .AuthenticationApi(configuration);

let body:.AuthenticationApiAuthDeletePostRequest = {
  // AuthDeletePostRequest
  authDeletePostRequest: {
    email: "email_example",
  },
};

apiInstance.authDeletePost(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authDeletePostRequest** | **AuthDeletePostRequest**|  |


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
**200** | User deleted successfully |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **authLoginPost**
> void authLoginPost(authLoginPostRequest)


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .AuthenticationApi(configuration);

let body:.AuthenticationApiAuthLoginPostRequest = {
  // AuthLoginPostRequest
  authLoginPostRequest: {
    email: "email_example",
    password: "password_example",
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

**void**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **authLogoutPost**
> void authLogoutPost()


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .AuthenticationApi(configuration);

let body:any = {};

apiInstance.authLogoutPost(body).then((data:any) => {
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
**200** | Successful logout |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **authRegisterPost**
> void authRegisterPost(authLoginPostRequest)


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .AuthenticationApi(configuration);

let body:.AuthenticationApiAuthRegisterPostRequest = {
  // AuthLoginPostRequest
  authLoginPostRequest: {
    email: "email_example",
    password: "password_example",
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
**201** | User registered successfully |  -  |
**400** | Bad request, invalid input |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)


