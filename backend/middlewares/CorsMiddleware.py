from falcon_cors import CORS

class CorsMiddleware(CORS):
    
    def __init__(self, allowed_origins_list):
        self.allowed_origins_list = allowed_origins_list
    
    def process_response(self, req, resp, resource, req_succeeded):
        origin = req.get_header('Origin')
        if origin in self.allowed_origins_list:
            resp.set_header('Access-Control-Allow-Origin', origin)
            resp.set_header('Access-Control-Allow-Methods', 'POST, DELETE')
            resp.set_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            resp.set_header('Access-Control-Max-Age', '3600')