import falcon
import jwt
import json
from db.database import User
import hashlib
from falcon_limiter.utils import register
from middlewares.RateLimiterMiddleware import RateLimitMiddleware

class AuthLoginResource:
    def __init__(self, db, secret_key):
        self.db = db
        self.secret_key = secret_key
    
    @RateLimitMiddleware.limiter.limit(["10 per hour", "1 per minute"])
    def on_post(self, req, resp):
        with self.db.Session() as session:
            try:
                data = json.loads(req.stream.read().decode('utf-8'))
                email = data['email']
                password = data['password']
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                
                user = session.query(User).filter_by(email=email).first()
                
                if user and user.password == hashed_password:
                    self.set_user_active(session, user)
                    token = self.generate_jwt_token(user)
                    resp.status = falcon.HTTP_200
                    resp.body = json.dumps({'message': 'Login successful', 'token': token})
                else:
                    resp.status = falcon.HTTP_401
                    resp.body = json.dumps({'error': 'Invalid email or password'})
            except KeyError as e:
                resp.status = falcon.HTTP_400
                resp.body = json.dumps({'error': f'Missing required parameter: {e}'})
            except Exception as e:
                resp.status = falcon.HTTP_500
                resp.body = json.dumps({'error': str(e)})
    
    def set_user_active(self, session, user):
        user.is_active = True
        session.commit()
    
    def generate_jwt_token(self, user):
        payload = {'user_id': user.id, 'email': user.email}
        return jwt.encode(payload, self.secret_key, algorithm='HS256')