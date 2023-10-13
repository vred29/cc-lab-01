import pandas as pd
import json
import uuid

# Read data from .xlsx file
data = pd.read_excel('./dataset/Netflix_Dataset_Latest_2021.xlsx')

# Take only the first 500 records
data = data.head(500)

# Select specific columns and rename them for better readability
data = data[[
    'Title',
    'Genre',
    'View Rating',
    'IMDb Score',
    'Rotten Tomatoes Score',
    'Metacritic Score',
    'Netflix Release Date',
    'Tags'
]]
data.columns = ['title', 'genre', 'view_rating', 'imdb_score', 'rotten_tomatoes_score', 'metacritic_score', 'netflix_release_date', 'tags']

# Convert columns to appropriate data types
data['genre'] = data['genre'].apply(lambda x: [item.strip() for item in x.split(',')] if isinstance(x, str) else [])
data['view_rating'] = pd.to_numeric(data['view_rating'], errors='coerce').fillna(0)
data['imdb_score'] = pd.to_numeric(data['imdb_score'], errors='coerce').fillna(0)
data['rotten_tomatoes_score'] = pd.to_numeric(data['rotten_tomatoes_score'], errors='coerce').fillna(0)
data['metacritic_score'] = pd.to_numeric(data['metacritic_score'], errors='coerce').fillna(0)
data['netflix_release_date'] = pd.to_datetime(data['netflix_release_date'])
data['tags'] = data['tags'].apply(lambda x: [item.strip() for item in x.split(',')] if isinstance(x, str) else [])

# Create a dictionary to hold the records with the desired keys
data_dict = {}

# Iterate over each record and create the desired key
for record in data.to_dict(orient='records'):
    # Generate a UUID
    record_uuid = str(uuid.uuid4())
    # Add the record to the dictionary with the desired key
    data_dict[record_uuid] = record

# Write the JSON data to a .json file
with open('movies.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4, default=str)  # Use default=str to handle datetime serialization
