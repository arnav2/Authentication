import falcon
import json

from db.models import User

class AuthLogoutResource:

    def __init__(self, db):
        self.db = db

    def on_post(self, req, resp):
        with self.db.Session() as session:
            try:
                data = json.loads(req.stream.read().decode('utf-8'))
                email = data['email']
                
                user = session.query(User).filter_by(email=email).first()
                if user:
                    self.set_user_inactive(user)
                    resp.status = falcon.HTTP_200
                    resp.body = json.dumps({'message': 'Logout successful'})
                else:
                    resp.status = falcon.HTTP_404
                    resp.body = json.dumps({'error': 'User not found'})
            except Exception as e:
                resp.status = falcon.HTTP_500
                resp.body = json.dumps({'error': str(e)})
    def set_user_inactive(self, user: User):
        user.is_active = False
        self.db.Session().commit()
