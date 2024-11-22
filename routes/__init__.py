from flask import Flask
from routes.admin import admin_routes

def register_routes(app : Flask):
    app.register_blueprint(admin_routes, url_prefix = '/admin')
