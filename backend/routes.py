import falcon
from backend.resources import AuthLoginResource, AuthRegisterResource

# Create Falcon API instance
api = falcon.API()

# Instantiate resource classes
auth_login_resource = AuthLoginResource()
auth_register_resource = AuthRegisterResource()

# Define routes
api.add_route('/auth/login', auth_login_resource)
api.add_route('/auth/register', auth_register_resource)
