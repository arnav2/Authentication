import unittest
import falcon
import json
import hashlib
from datetime import datetime
from unittest.mock import MagicMock, patch

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from resources.AuthRegisterResource import AuthRegisterResource
from db.database import User

class TestAuthRegisterResource(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.resource = AuthRegisterResource(self.db_mock)
        self.email = 'test@example.com'
        self.password = 'password123'
        self.resp = MagicMock()

    def test_valid_registration(self):
        # Mock request data
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': self.email, 'password': self.password})

        # Mock database query (user not found)
        self.db_mock.Session().__enter__().query().filter_by().first.return_value = None

        # Invoke resource method
        self.resource.on_post(req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_201)
        self.assertEqual(self.resp.body, json.dumps({'message': 'Registration successful'}))

        # Verify database interaction
        self.db_mock.Session().__enter__().add.assert_called_once()
        self.db_mock.Session().__enter__().commit.assert_called_once()

    def test_invalid_registration_user_exists(self):
        # Mock request data
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': self.email, 'password': self.password})

        # Mock database query (user already exists)
        self.db_mock.Session().__enter__().query().filter_by().first.return_value = User(email=self.email, password=self.password)

        # Invoke resource method
        self.resource.on_post(req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_409)
        self.assertEqual(self.resp.body, json.dumps({'error': 'Username already exists. Please try logging in'}))

        # Verify no database interaction
        self.assertFalse(self.db_mock.Session().__enter__().add.called)
        self.assertFalse(self.db_mock.Session().__enter__().commit.called)

    def test_missing_parameter(self):
        # Mock request data with missing parameter
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': self.email})

        # Invoke resource method
        self.resource.on_post(req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_400)
        self.assertIn('error', json.loads(self.resp.body))
        self.assertIn('Missing required parameter', json.loads(self.resp.body)['error'])

    def test_exception_handling(self):
        # Mock request data
        req = MagicMock()
        req.stream.read.side_effect = Exception('Test exception')

        # Invoke resource method
        self.resource.on_post(req, self.resp)

        # Assertions
        self.assertEqual(self.resp.status, falcon.HTTP_500)
        self.assertIn('error', json.loads(self.resp.body))
        self.assertIn('Test exception', json.loads(self.resp.body)['error'])

if __name__ == '__main__':
    unittest.main()
