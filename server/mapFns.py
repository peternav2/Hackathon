import pandas as pd
import requests
import os
from dotenv import load_dotenv
load_dotenv()
map_key = os.getenv("MAP_KEY", "Key Not Found")
df_usa = pd.read_csv("../usa_data.csv", low_memory=False)
df_zips = pd.read_csv("../zip_codes.csv", low_memory=False)

def getAddsInState(state):
    df_adds = df_usa[df_usa['address'].str.contains(state)]
    return df_adds

def getZipInState(state):
    df_temp = df_zips[df_zips['state_name'].str.contains(state)]





def getAddsInZip(zip):
    df_adds = df_usa[df_usa['address'].str.contains(zip)]
    return df_adds

def getBestAdds(zip):
    df_adds = getAddsInZip(zip)
    df_best = df_adds[df_adds['rating'].str.contains(pat="4\.[0-9]+|5\.0", regex=True)]
    tempadds = []
    for row in df_best.iterrows():
        tempadds.append(df_usa["address"][row[0]])
        print(df_usa["address"][row[0]])
        print("\n")
    return df_best
    
def get_coordinates_from_address(address):
    API_KEY = map_key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    
    # URL encode the address
    address = requests.utils.quote(address)
    
    # Complete URL
    url = f"{base_url}address={address}&key={API_KEY}"
    
    # Send the request
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if any results were found
        if data['status'] == 'OK':
            # Extract latitude and longitude
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            return latitude, longitude
        else:
            print("Geocoding API error:", data['status'])
            return None, None
    else:
        print("HTTP error", response.status_code)
        return None, None
# print(getBestAdds("11561"))
# AddsCoords = []
# for add in getBestAdds("10001").iterrows():
#     AddsCoords.append(get_coordinates_from_address(df_usa["address"][add[0]]))
# for coord in AddsCoords:
#     print(coord)
#     print("\n")