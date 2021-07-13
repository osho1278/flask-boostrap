from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class account(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    username = db.Column(db.String(200))
    date_joined = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean,default=True)
    is_staff = db.Column(db.Boolean,default=False)
    is_superuser = db.Column(db.Boolean,default=False)
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
        # self.date_joined = pin
