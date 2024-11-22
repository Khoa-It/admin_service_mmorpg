from flask import Flask
from routes import register_routes

app = Flask(__name__)
register_routes(app)

@app.route('/')
def application_index():
    return 'Welcome to flask application ! - this is python'

if __name__ == '__main__' :
    app.run(debug=True)