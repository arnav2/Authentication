import falcon
import json
import unittest
from unittest.mock import MagicMock

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from db.database import User
from resources.AuthDeleteResource import AuthDeleteResource

class TestAuthDeleteResource(unittest.TestCase):

    def setUp(self):
        self.db_mock = MagicMock()
        self.user_email = 'test@example.com'
        self.user_password = 'password123'
        self.user = User(email=self.user_email, password=self.user_password)
        self.db_mock.Session.return_value.__enter__.return_value.query.return_value.filter_by.return_value.first.return_value = self.user

    def test_delete_user_success(self):
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': self.user_email})
        resp = MagicMock()

        resource = AuthDeleteResource(self.db_mock)
        resource.on_post(req, resp)

        self.assertEqual(resp.status, falcon.HTTP_200)
        self.assertEqual(json.loads(resp.body), {'message': 'User deleted successfully'})

    def test_delete_user_not_found(self):
        # Test deleting a user that does not exist
        non_existent_user_email = 'nonexistent@example.com'
        self.db_mock.Session.return_value.__enter__.return_value.query.return_value.filter_by.return_value.first.return_value = None

        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': non_existent_user_email})
        resp = MagicMock()

        resource = AuthDeleteResource(self.db_mock)
        resource.on_post(req, resp)

        self.assertEqual(resp.status, falcon.HTTP_404)
        self.assertEqual(json.loads(resp.body), {'error': 'User not found'})

    def test_missing_email_in_request(self):
        # Test handling request without email
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({})
        resp = MagicMock()

        resource = AuthDeleteResource(self.db_mock)
        resource.on_post(req, resp)

        self.assertEqual(resp.status, falcon.HTTP_400)
        self.assertIn('Missing email', resp.body)

    def test_invalid_json_request_body(self):
        # Test handling request with invalid JSON
        req = MagicMock()
        req.stream.read.return_value.decode.return_value = 'invalid_json'
        resp = MagicMock()

        resource = AuthDeleteResource(self.db_mock)
        resource.on_post(req, resp)
        self.assertEqual(resp.status, falcon.HTTP_400)
        self.assertIn('Invalid JSON', resp.body)

    def test_database_error(self):
        # Test handling database error during user deletion
        self.db_mock.Session.return_value.__enter__.return_value.commit.side_effect = Exception('Database error')

        req = MagicMock()
        req.stream.read.return_value.decode.return_value = json.dumps({'email': self.user_email})
        resp = MagicMock()

        resource = AuthDeleteResource(self.db_mock)
        resource.on_post(req, resp)

        self.assertEqual(resp.status, falcon.HTTP_500)
        self.assertIn('Failed to delete user', resp.body)

if __name__ == '__main__':
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    unittest.main()
