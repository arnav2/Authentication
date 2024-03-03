

from db.db_config import Config
# Get the absolute path of the python_sdk directory
python_sdk_path = os.path.abspath("python_sdk")

# Add the python_sdk directory to the Python path
sys.path.append(python_sdk_path)

from openapi_client.api.default_api import DefaultApi
from openapi_client.models import AuthLoginPostRequest, AuthLoginPost200Response

# Prepare test data (replace with actual test data)
login_request = AuthLoginPostRequest(
    email="test@example.com",
    password="password123"
)

class AuthResource:
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

# Initialize Falcon application
app = falcon.App()
# Add routes
app.add_route('/auth/login', AuthResource())

# Start Falcon server
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    print("Falcon server started on http://127.0.0.1:8000/")
    httpd.serve_forever()
    