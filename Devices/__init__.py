from flask import Flask, redirect, url_for
from Auth import Authenticator
class Devices:
    def __init__(self,app):
        self.app = app
        self.authenticator=Authenticator()

    def add_route(self):
        @self.app.route('/devices')
        @self.authenticator.token_required
        def getDevices(self):
            return 'Hello Devices'