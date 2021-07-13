from flask import Flask, redirect, url_for
from User import User
from Devices import Devices
from Auth.Login import Login
from Auth.Signup import Signup

class Api:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Pass2020!@localhost/telemetry"
        self.auth=Login(self.app)
        self.signup=Signup(self.app)
        self.user=User(self.app)
        self.devices=Devices(self.app)
    def run(self):
        self.app.run(debug = True)

    def add_route(self):
        self.auth.add_route()
        self.signup.add_route()
        self.user.add_route()
        self.devices.add_route()



if __name__ == '__main__':
   api=Api()
   api.add_route()
   api.run()