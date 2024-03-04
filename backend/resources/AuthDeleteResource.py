import falcon
import json
from db.models import User
import sqlalchemy
from falcon_limiter.utils import register
from middlewares.RateLimiterMiddleware import RateLimitMiddleware
class AuthDeleteResource:
    def __init__(self, db):
        self.db = db
    
    @register(RateLimitMiddleware.limiter.limit(["10 per hour", "3 per minute"]))
    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read().decode('utf-8'))
            email = data.get('email')
            if not email:
                raise falcon.HTTPBadRequest('Missing email', 'Email is required in the request body')

            with self.db.Session() as session:
                user = session.query(User).filter_by(email=email).first()
                if user:
                    try:
                        session.delete(user)
                        session.commit()
                        resp.status = falcon.HTTP_200
                        resp.body = json.dumps({'message': 'User deleted successfully'})
                    except sqlalchemy.exc.SQLAlchemyError as e:
                        session.rollback()  # Roll back the transaction
                        resp.status = falcon.HTTP_500
                        resp.body = json.dumps({'error': 'Failed to delete user: ' + str(e)})
                else:
                    resp.status = falcon.HTTP_404
                    resp.body = json.dumps({'error': 'User not found'})
        except json.JSONDecodeError:
            resp.status = falcon.HTTPBadRequest('Invalid JSON', 'Unable to decode JSON from request body')
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({'error': str(e)})
