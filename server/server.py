import json
from flask import Flask, make_response, request
import flask
from flask_cors import CORS, cross_origin
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
# @cross_origin()
def hello():
    if request.method == 'POST':
        res = make_response()
        print(request.json)
        x = 3
        res.response = json.dumps({"message": "Hello, World! WE POSTING"})
        res.headers['content-type'] = 'application/json'
        return res
    else:
        res = make_response()
        res.response = json.dumps({"message": "Hello, World! WE GETTING"})
        return res
