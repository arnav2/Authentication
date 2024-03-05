import unittest
import falcon
import json
from unittest.mock import MagicMock, patch

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from resources.AuthLogoutResource import AuthLogoutResource

class TestAuthLogoutResource(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.resource = AuthLogoutResource(self.db_mock)
        self.email = 'test@example.com'
        self.resp = MagicMock()

    def test_valid_logout(self):
        # Mock request data
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': self.email})

        # Mock database query
        user_mock = MagicMock()
        self.db_mock.Session().__enter__().query().filter_by().first.return_value = user_mock

        # Invoke resource method
        self.resource.on_post(req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_200)
        self.assertEqual(self.resp.body, json.dumps({'message': 'Logout successful'}))

        # Verify database interaction
        self.assertFalse(user_mock.is_active)
        self.db_mock.Session().__enter__().commit.assert_called_once()

    def test_invalid_logout_user_not_found(self):
        # Mock request data
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': self.email})

        # Mock database query (user not found)
        self.db_mock.Session().__enter__().query().filter_by().first.return_value = None

        # Invoke resource method
        self.resource.on_post(req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_404)
        self.assertEqual(self.resp.body, json.dumps({'error': 'User not found'}))

    def test_exception_handling(self):
        # Mock request data
        req = MagicMock()
        req.stream.read.side_effect = Exception('Test exception')

        # Invoke resource method
        self.resource.on_post(req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_500)
        self.assertEqual(self.resp.body, json.dumps({'error': 'Test exception'}))

if __name__ == '__main__':
    unittest.main()
