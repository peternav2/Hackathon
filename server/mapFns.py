import pandas as pd
import requests
import os
from dotenv import load_dotenv
load_dotenv()
map_key = os.getenv("MAP_KEY", "Key Not Found")
df_usa = pd.read_csv("../usa_data.csv", low_memory=False)
df_zips = pd.read_csv("./uszips.csv", low_memory=False)
def get_coordinates_from_address(address):
    API_KEY = map_key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    address = "1600 Amphitheatre Parkway, Mountain View, CA"

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

# st = "NY"
def getBest5FromState(state):
    mask = df_zips['state_id'].str.contains(state)
    df_ny_zips = df_zips[mask]['zip']
    zipcode = df_ny_zips.sample(1).iloc[0]
    mask = df_usa['address'].str.contains(zipcode.__str__())
    df_ny_adds = df_usa[mask]
    mask = df_ny_adds['rating'].str.contains(pat="4\.[0-9]+|5\.0", regex=True)
    df_ny_adds = df_ny_adds[mask]
    # mask = df_ny_adds['reviews_count'].str.contains(pat="/^.{5,}$/", regex=True)
    # df_ny_adds = df_ny_adds[mask]
    print(len(df_ny_adds.head(5)))
    return df_ny_adds.head(5)
# while (True):
#     best = getBest5FromState(st)
#     if best is None:
#         continue
#     if len(best) < 5:
#         continue
#     else:
#         break
# getBest5FromState(st)
# # print(best)
# adds = []
# for row in best.iterrows():
#     adds.append(df_usa["address"][row[0]])
#     print(df_usa["address"][row[0]])
#     print("\n")
# AddsCoords = []
# for add in adds:
#     latitude, longitude = get_coordinates_from_address(add.__str__())
#     AddsCoords.append((latitude, longitude))
# for coord in AddsCoords:
#     print(coord)
#     print("\n")



# adds = best['address']
# for add in adds:
#     print(add[0])
# print(adds[1])

# # print(df_ny_zips)
# # print("your zip is: "+ zipcode.__str__() + "\n")
# # regex = r"^(50\.0|[5-9]\d(\.\d+)?)$"
# exit(1)




























# # def getAddsInState(state):
# #     df_adds = df_usa[df_usa['address'].str.contains(state)]
# #     return df_adds
# # def getZipInState(state):
# #     df_temp = df_zips[df_zips['state_name'].str.contains(state)]
# #     print(df_temp)
# #     return df_temp
# # def getRandomZip(df_state_zips):
# #     return df_state_zips.sample(5)
# # print("testing geting random zip")
# # zips = getRandomZip(getZipInState("NY"))
# # print(zips)





# # def getAddsInZip(zip):
# #     df_adds = df_usa[df_usa['address'].str.contains(zip)]
# #     return df_adds

# # def getBestAdds(zip):
# #     df_adds = getAddsInZip(zip)
# #     df_best = df_adds[df_adds['rating'].str.contains(pat="4\.[0-9]+|5\.0", regex=True)]
# #     tempadds = []
# #     for row in df_best.iterrows():
# #         tempadds.append(df_usa["address"][row[0]])
# #         print(df_usa["address"][row[0]])
# #         print("\n")
# #     return df_best
    

# # print(getBestAdds("11561"))
# # AddsCoords = []
# # for add in getBestAdds("10001").iterrows():
# #     AddsCoords.append(get_coordinates_from_address(df_usa["address"][add[0]]))
# # for coord in AddsCoords:
# #     print(coord)
# #     print("\n")