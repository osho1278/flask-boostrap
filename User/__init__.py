from flask import Flask, redirect, url_for
class User:
    def __init__(self,app):
        self.app = app

    def add_route(self):
        @self.app.route('/users')
        def getUsers():
            return 'Hello Admin'