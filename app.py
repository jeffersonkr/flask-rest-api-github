from flask import Flask
from apis import api

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
