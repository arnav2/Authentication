# coding: utf-8

"""
    Basic API

    A basic API for demonstration purposes

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.hello_get200_response import HelloGet200Response

class TestHelloGet200Response(unittest.TestCase):
    """HelloGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HelloGet200Response:
        """Test HelloGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HelloGet200Response`
        """
        model = HelloGet200Response()
        if include_optional:
            return HelloGet200Response(
                message = 'Hello, World!'
            )
        else:
            return HelloGet200Response(
        )
        """

    def testHelloGet200Response(self):
        """Test HelloGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()