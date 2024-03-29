# coding: utf-8

"""
    Authentication System API

    API for user authentication and management

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.auth_login_post200_response import AuthLoginPost200Response

class TestAuthLoginPost200Response(unittest.TestCase):
    """AuthLoginPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthLoginPost200Response:
        """Test AuthLoginPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthLoginPost200Response`
        """
        model = AuthLoginPost200Response()
        if include_optional:
            return AuthLoginPost200Response(
                access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
            )
        else:
            return AuthLoginPost200Response(
        )
        """

    def testAuthLoginPost200Response(self):
        """Test AuthLoginPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
