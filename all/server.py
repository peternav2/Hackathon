from flask import Flask, make_response, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
from random import choice
import json
app = Flask(__name__)
CORS(app)
# Load the data
df = pd.read_csv('/Users/anyakozhevatova/Hackathon/all/cleaned_data.csv')

def get_locations_by_state(dataframe, state_abbr):
    # Filter locations by state abbreviation in the address
    state_filtered_df = dataframe[dataframe['address'].str.contains(rf'\b{state_abbr}\b', regex=True)]
    
    # Extract zip codes
    zip_codes = state_filtered_df['address'].str.extract(r'(\d{5})')[0].unique()
    
    # Check if any zip codes were found; if not, return None and an empty DataFrame
    if len(zip_codes) == 0:
        return None, pd.DataFrame()
    
    # Randomly select a zip code
    selected_zip_code = choice(zip_codes)
    
    # Filter locations within the selected zip code
    zip_code_filtered_df = state_filtered_df[state_filtered_df['address'].str.contains(selected_zip_code)]
    
    # Convert rating to numeric and filter for ratings between 4.0 and 5.0
    zip_code_filtered_df['rating'] = pd.to_numeric(zip_code_filtered_df['rating'], errors='coerce')
    zip_code_filtered_df = zip_code_filtered_df[(zip_code_filtered_df['rating'] >= 4.0) & (zip_code_filtered_df['rating'] <= 5.0)]
    
    # Convert reviews_count to numeric for sorting
    zip_code_filtered_df['reviews_count'] = pd.to_numeric(zip_code_filtered_df['reviews_count'], errors='coerce')
    
    # Sort by reviews_count and rating, then select the top 5
    top_locations = zip_code_filtered_df.sort_values(by=['reviews_count', 'rating'], ascending=[False, False]).head(5)
    
    return selected_zip_code, top_locations[['name', 'category', 'address', 'reviews_count', 'rating']]

# @app.route('/')
# @cross_origin()
# def index():
#     return render_template('index.html')

@app.route('/get_locations/', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin()
def get_locations():
    if request.method == 'POST':
        res = make_response()
        state_abbr = request.form['state']
        selected_zip_code, top_locations = get_locations_by_state(df, state_abbr)
        # Convert DataFrame to HTML table; easier for quick demonstration
        if selected_zip_code and not top_locations.empty:
            top_locations_html = top_locations.to_html(classes='table table-striped', index=False, justify='left')
        else:
            top_locations_html = "<div>No locations found for the selected state or zip code.</div>"
        res.headers['Content-Type'] = 'application/json'
        res.response = json.dumps({'zip_code': selected_zip_code or "Not Found", 'top_locations': top_locations_html})
        return res
        # return jsonify(zip_code=selected_zip_code or "Not Found", top_locations=top_locations_html)
    else:
        res = make_response()
        res.response = json.dumps({"message": "Hello We are her"})
        return res

if __name__ == '__main__':
    app.run(debug=True)