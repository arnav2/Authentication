import falcon
import jwt  # Assuming you're using JWT for access tokens
from falcon.media.validators import jsonschema

class AuthLoginResource:
    def on_post(self, req, resp):
        email = req.media['email']
        password = req.media['password']

        # Authenticate user (implement your authentication logic here)
        if self.authenticate_user(email, password):
            # Generate JWT access token
            access_token = self.generate_access_token(email)

            resp.status = falcon.HTTP_200
            resp.media = {'accessToken': access_token}
        else:
            resp.status = falcon.HTTP_401

    def authenticate_user(self, email: str, password: str) -> bool:
        return True
    
    def generate_access_token(self, email: str):
        return "Test access Token"