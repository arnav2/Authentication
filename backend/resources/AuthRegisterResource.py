import falcon
import json
import hashlib
from datetime import datetime
from db.database import User
from falcon_limiter.utils import register
from middlewares.RateLimiterMiddleware import RateLimitMiddleware
class AuthRegisterResource:
    def __init__(self, db):
        self.db = db

    @register(RateLimitMiddleware.limiter.limit(["10 per hour", "3 per minute"]))
    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read().decode('utf-8'))
            email = data['email']
            password = data['password']
        except KeyError as e:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'error': f'Missing required parameter: {e}'})
            return
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({'error': str(e)})
            return
        
        with self.db.Session() as session:
            try:
                self.register_user(session, resp, email, password)
            except KeyError as e:
                resp.status = falcon.HTTP_400
                resp.body = json.dumps({'error': f'Missing required parameter: {e}'})
            except Exception as e:
                resp.status = falcon.HTTP_500
                resp.body = json.dumps({'error': str(e)})

    def register_user(self, session, resp, email, password):
        user = session.query(User).filter_by(email=email).first()
        if user:
            resp.status = falcon.HTTP_409
            resp.body = json.dumps({'error': 'Username already exists. Please try logging in'})
            return
        
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        new_user = User(email=email, password=hashed_password, created_at=datetime.now(), is_active=True)
        session.add(new_user)
        session.commit()
        
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({'message': 'Registration successful'})
