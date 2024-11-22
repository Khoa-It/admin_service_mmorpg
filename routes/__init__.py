from flask import Flask
from routes.admin import *

def register_routes(app = Flask(__name__)):
    app.register_blueprint(admin_routes)
