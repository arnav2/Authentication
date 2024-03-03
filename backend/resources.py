import falcon
import os
import sys
import psycopg2
from db.db_config import Config



class AuthLoginResource:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )
        self.api = DefaultApi()

    def on_post(self, req, resp):
        # Parse request body
        login_data = req.media
        print("login_data: ", login_data)
        
        # Create AuthLoginPostRequest object
        login_request = AuthLoginPostRequest(
            email=login_data['email'],
            password=login_data['password']
        )

        # Call the auth_login_post function
        response = self.api.auth_login_post(auth_login_post_request=login_request)

        # Return appropriate response
        if isinstance(response, AuthLoginPost200Response):
            resp.status = falcon.HTTP_200
            resp.media = {"access_token": response.access_token}
        else:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Login failed"}