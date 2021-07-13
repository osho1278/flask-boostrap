from flask import Flask, request,redirect,jsonify, url_for,make_response
from datetime import datetime, timedelta
import jwt

class Login:
    def __init__(self, app):
        self.app = app

    def add_route(self):
        @self.app.route('/login', methods=['POST'])
        def Login():
            auth = request.json
            print(auth)
            if not auth or not auth.get('email') or not auth.get('password'):
                # returns 401 if any email or / and password is missing
                return make_response(
                    'Could not verify',
                    401,
                    {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
                )
            if True: #check_password_hash(user.password, auth.get('password')):
                # generates the JWT Token
                token = jwt.encode({
                    'public_id': "osho",
                    'exp': datetime.utcnow() + timedelta(minutes=30)
                }, 'SECRET_KEY')

                return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
            # returns 403 if password is wrong
            return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
            )
