import unittest
import falcon
import json
import hashlib
from unittest.mock import Mock, patch, MagicMock

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from db.database import User
from resources.AuthLoginResource import AuthLoginResource

class TestAuthLoginResource(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.secret_key = 'secret'
        self.resource = AuthLoginResource(self.db_mock, self.secret_key)
        self.email = 'test@example.com'
        self.password = 'password123'
        self.token = 'test_token'
        self.resource.generate_jwt_token = Mock(return_value=self.token)
        
        self.hashed_password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        self.user = User(email=self.email, password=self.hashed_password)
        
        # Mock request data
        self.req = MagicMock()
        self.req.stream.read.return_value.decode.return_value = json.dumps({'email': self.email, 'password': self.password})
        self.resp = MagicMock()
        
    def test_valid_login(self):
        self.db_mock.Session().__enter__().query().filter_by().first.return_value = self.user
        
        # Invoke resource method
        self.resource.on_post(self.req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_200)
        self.assertEqual(self.resp.body, json.dumps({'message': 'Login successful', 'token': self.token}))

        # Verify database interaction
        self.assertTrue(self.user.is_active)
        self.db_mock.Session.return_value.__enter__.return_value.commit.assert_called_once()

    def test_invalid_login(self):
        # Mock request data
        self.req.stream.read = Mock(return_value=json.dumps({'email': 'test@example.com', 'password': 'invalid'}).encode('utf-8'))

        # Mock database query
        self.db_mock.Session().__enter__().query().filter_by().first.return_value = None

        # Invoke resource method
        self.resource.on_post(self.req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_401)
        self.assertEqual(self.resp.body, json.dumps({'error': 'Invalid email or password'}))

    def test_missing_parameter(self):
        # Mock request data with missing parameter
        self.req.stream.read = Mock(return_value=json.dumps({'email': 'test@example.com'}).encode('utf-8'))

        # Invoke resource method
        self.resource.on_post(self.req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_400)
        self.assertIn('error', json.loads(self.resp.body))
        self.assertIn('Missing required parameter', json.loads(self.resp.body)['error'])

    def test_exception_handling(self):
        # Mock request data
        self.req.stream.read = Mock(side_effect=Exception('Test exception'))

        # Invoke resource method
        self.resource.on_post(self.req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_500)
        self.assertIn('error', json.loads(self.resp.body))
        self.assertIn('Test exception', json.loads(self.resp.body)['error'])

if __name__ == '__main__':
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    unittest.main()