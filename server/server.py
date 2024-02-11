import json
import os
import requests
from dotenv import load_dotenv
from flask import Flask, make_response, request
import flask
from flask_cors import CORS, cross_origin
from flask import Flask
from flask_cors import CORS
from mapFns import *
app = Flask(__name__)
CORS(app)
load_dotenv()
map_key = os.getenv("MAP_KEY", "Key Not Found")


@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
@cross_origin()
def hello():
    if request.method == 'POST':
        body = request.get_json()
        location = body['state']
        while (True):
            best = getBest5FromState(location)
            if best is None:
                continue
            if len(best) < 5:
                continue
            else:
                break
        #getBest5FromState(location)
        print("PRINT BEST 5")
        print(best)
        adds = []
        for row in best.iterrows():
            adds.append(df_usa["address"][row[0]])
            print(df_usa["address"][row[0]])
            print("\n")
        addsCoords = []
        for add in adds:
            print("PRINTING ADD")
            print(add.__str__())
            print("\n")
            print("PRINTING COORDS")
            print(get_coordinates_from_address(add))
            latitude, longitude = get_coordinates_from_address(add.__str__())
            addsCoords.append((latitude, longitude))
        for coord in addsCoords:
            print(coord)
            print("\n")        
        res = make_response()
        res.response = json.dumps({'coords': addsCoords})
        res.headers['content-type'] = 'application/json'
        return res
    else:
        res = make_response()
        #coords = get_coordinates_from_address("1600 Amphitheatre Parkway, Mountain View, CA")
        res.response = json.dumps({"message": "Hello, World!"})
        return res
    








