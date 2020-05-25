from flask import Flask
from flask_restplus import Resource, Api
from flask import jsonify
import requests
from apis import api
import subprocess, os

app = Flask(__name__)
app.config['MYSQL_HOST'] = "database"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "secret"
app.config['MYSQL_DB'] = "captalys"
app.config['MYSQL_PORT'] = 3306

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
