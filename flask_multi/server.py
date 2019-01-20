from flask import Flask


server = Flask(__name__)

@server.route('/')
def index():
    return 'Hello Flask app'
