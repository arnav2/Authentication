# AuthLoginPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT access token | [optional] 

## Example

```python
from openapi_client.models.auth_login_post200_response import AuthLoginPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLoginPost200Response from a JSON string
auth_login_post200_response_instance = AuthLoginPost200Response.from_json(json)
# print the JSON string representation of the object
print AuthLoginPost200Response.to_json()

# convert the object into a dict
auth_login_post200_response_dict = auth_login_post200_response_instance.to_dict()
# create an instance of AuthLoginPost200Response from a dict
auth_login_post200_response_form_dict = auth_login_post200_response.from_dict(auth_login_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


