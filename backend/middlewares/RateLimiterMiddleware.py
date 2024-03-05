import falcon
from falcon_limiter import Limiter
import time
import bisect
def get_access_route_addr(req, resp, resource, params) -> str:
        return req.access_route[0] if req.access_route else req.remote_addr

class RateLimitMiddleware:
    limiter = Limiter(
        key_func=get_access_route_addr,
        default_limits="5 per minute, 2 per second"
    )
    
    def process_request(self, req, resp):
        # Initialize req.context if not already initialized
        if not hasattr(req, 'context'):
            req.context = {}
        # Set the ratelimit_key in the request context
        req.context['ratelimit_key'] = RateLimitMiddleware.limiter.key_func(req, resp, None, None)

        # Retrieve limits for the key
        limits = RateLimitMiddleware.limiter.get_limits(req.context['ratelimit_key'])
        
        # Calculate remaining tokens
        remaining_tokens = self.calculate_remaining_tokens(limits)
        print(f"Remaining tokens: {remaining_tokens}")
        
    def calculate_remaining_tokens(self, limits):
        # Extract the limit values and window size
        window_size = limits[0][1]
        max_requests = limits[0][0]
        
        # Calculate the current time
        current_time = time.time()
        
        # Calculate the number of tokens consumed in the current window
        tokens_consumed = max_requests - (len(limits[1]) - bisect.bisect_left(limits[1], current_time))
        
        # Calculate remaining tokens
        remaining_tokens = max_requests - tokens_consumed
        
        return remaining_tokens
        
    def process_resource(self, req, resp, resource, req_succeeded):
        print('Response status: ', resp.status)
        if req_succeeded and resp.status == falcon.HTTP_429:
            # Handle rate limit exceeded error
            resp.body = 'Rate limit exceeded. Please try again later.'