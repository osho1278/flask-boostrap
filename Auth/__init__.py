
# flask imports
from flask import Flask, request, jsonify, make_response
# from flask_sqlalchemy import SQLAlchemy
import uuid # for public id
import jwt
from datetime import datetime, timedelta
from functools import wraps

# app.config['SECRET_KEY'] = 'your secret key'

class Authenticator:
    def token_required(self,f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            # jwt is passed in the request header
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            # return 401 if token is not passed
            if not token:
                return jsonify({'message' : 'Token is missing !!'}), 401
    
            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, 'SECRET_KEY')
                current_user = data
            except:
                return jsonify({
                    'message' : 'Token is invalid !!'
                }), 401
            # returns the current logged in users contex to the routes
            return  f(current_user, *args, **kwargs)
        return decorated
  