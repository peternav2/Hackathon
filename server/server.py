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
    


# @cross_origin()
# def get_coordinates_from_addresses(addresses):
#     for address in addresses:
#         API_KEY = map_key
#         base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
#         # URL encode the address
#         address = requests.utils.quote(address)
#         # Complete URL
#         url = f"{base_url}address={address}&key={API_KEY}"
#         # Send the request
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Parse the JSON response
#             data = response.json()
            
#             # Check if any results were found
#             if data['status'] == 'OK':
#                 # Extract latitude and longitude
#                 latitude = data['results'][0]['geometry']['location']['lat']
#                 longitude = data['results'][0]['geometry']['location']['lng']
#                 return latitude, longitude
#             else:
#                 print("Geocoding API error:", data['status'])
#                 return None, None
#         else:
#             print("HTTP error", response.status_code)
#             return None, None

# @cross_origin()
# def get_coordinates_from_address(address):
#     address = "1600 Amphitheatre Parkway, Mountain View, CA"
#     API_KEY = map_key
#     base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    
#     # URL encode the address
#     address = requests.utils.quote(address)
    
#     # Complete URL
#     url = f"{base_url}address={address}&key={API_KEY}"
    
#     # Send the request
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()
        
#         # Check if any results were found
#         if data['status'] == 'OK':
#             # Extract latitude and longitude
#             latitude = data['results'][0]['geometry']['location']['lat']
#             longitude = data['results'][0]['geometry']['location']['lng']
#             return latitude, longitude
#         else:
#             print("Geocoding API error:", data['status'])
#             return None, None
#     else:
#         print("HTTP error", response.status_code)
#         return None, None

# # Example usage
# address = "1600 Amphitheatre Parkway, Mountain View, CA"
# latitude, longitude = get_coordinates_from_address(address)
# if latitude and longitude:
#     print(f"Coordinates for '{address}' are: {latitude}, {longitude}")
# else:
#     print("Could not get the coordinates.")






