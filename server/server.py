from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins.

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Dummy function to simulate retrieving data based on the state
# Replace this with your actual function to retrieve data from your source
def get_random_zip_and_locations(state_abbr):
    # Placeholder for where you would have logic to get random zip code and locations
    # In practice, this function would interact with a database or data file
    if state_abbr == "NY":
        selected_zip = "10001"
        top_locations = [
            {"name": "Empire State Building", "lat": 40.748817, "lng": -73.985428},
            {"name": "Central Park", "lat": 40.7829, "lng": -73.9654},
            # ... more locations
        ]
    else:
        selected_zip = None
        top_locations = []

    return selected_zip, top_locations

@app.route("/get_locations", methods=['POST'])
def get_locations():
    # Get state from the request data
    state_data = request.get_json()
    state_abbr = state_data.get('state', '').upper()

    # Get a random zip code and top locations for the given state
    selected_zip, top_locations = get_random_zip_and_locations(state_abbr)

    # Return the data as a JSON response
    if selected_zip and top_locations:
        return jsonify({"zip_code": selected_zip, "locations": top_locations})
    else:
        return jsonify({"message": f"No locations found for state: {state_abbr}"}), 404

if __name__ == "__main__":
    app.run(debug=True)
