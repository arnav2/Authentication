import falcon
from falcon_apispec import FalconPlugin
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from wsgiref import simple_server
import os

from middlewares.RateLimiterMiddleware import RateLimitMiddleware

from resources.AuthRegisterResource import AuthRegisterResource
from resources.AuthLoginResource import AuthLoginResource
from resources.AuthLogoutResource import AuthLogoutResource
from resources.AuthDeleteResource import AuthDeleteResource

from resources.MetricsResource import MetricsResource

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), 'db', '.env'))

from db.database import Database

SECRET_KEY = os.getenv('SECRET_KEY')

app = falcon.API()
db = Database()

# Initialize Falcon plugin for generating OpenAPI Specification
spec = APISpec(
    title='Authentication APIs',
    version='1.0.0',
    openapi_version='3.0.0',
    plugins=[MarshmallowPlugin(), FalconPlugin(app)],
)

register_resource = AuthRegisterResource(db)
login_resource = AuthLoginResource(db, secret_key=SECRET_KEY)
logout_resource = AuthLogoutResource(db)
delete_resource = AuthDeleteResource(db)

app.add_route('/auth/register', register_resource)
app.add_route('/auth/login', login_resource)
app.add_route('/auth/logout', logout_resource)
app.add_route('/auth/delete', delete_resource)

app.add_route('/metrics', MetricsResource())

httpd = simple_server.make_server('127.0.0.1', 8000, app)
print(f'Falcon server started on http://localhost:8000/')
httpd.serve_forever()
