import falcon
from falcon.media.validators import jsonschema
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from openapi.python_sdk.openapi_client.api.default_api import DefaultApi
from openapi.python_sdk.openapi_client.models.auth_login_post_request import AuthLoginPostRequest
from backend.models import User
class AuthRegisterResource:
    
    def __init__(self):
        self.api = DefaultApi()
    
    def on_post(self, req, resp):
        email = req.media.get('email')
        password = req.media.get('password')

        auth_login_post_request = AuthLoginPostRequest(email="test@email.com", password="password123")
        
        try:
            response = self.api.auth_register_post(auth_login_post_request=AuthLoginPostRequest(email="test@email.com", password="password123"))
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_500
            resp.media = {'Unexpected Server Error: ': str(e)}
            return

        if response.status == 201:
            if store_user_in_database(email, password):
                resp.status = falcon.HTTP_201
            else:
                resp.status = falcon.HTTP_500
                resp.media = {'error': 'Failed to store user in the database'}
        else:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'Registration failed'}

def store_user_in_database(email: str, password: str):
    return True
    # engine = create_engine(DATABASE_URL)

    # Session = sessionmaker(bind=engine)
    # session = Session()
    # current_timestamp = datetime.now()
    # try:
    #     user = User(
    #         email=email,
    #         password=password,
    #         created_at=current_timestamp
    #     )
    #     session.add(user)
    #     session.commit()
    #     return True
    # except Exception as e:
    #     session.rollback()
    #     print(f"Error storing user in database: {e}")
    #     return False