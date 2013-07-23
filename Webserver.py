import os
from flask import Flask

app = Flask(__name__)

@app.route('/lo')
def hello():
    return 'Hello World!'


