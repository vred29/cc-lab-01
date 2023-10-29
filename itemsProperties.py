from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *

client = RecombeeClient(
  'lab01-movies',
  '4n1qnl6MbwhopsLr61jV8uxK3jnYBHswPJV8OV7Qg5vzd5ezJ2vezjZ7fYmjIiAl',
  region=Region.EU_WEST
)
# Define item properties
client.send(AddItemProperty('title', 'string'))
client.send(AddItemProperty('genre', 'set'))
client.send(AddItemProperty('view_rating', 'set'))
client.send(AddItemProperty('imdb_score', 'double'))
client.send(AddItemProperty('rotten_tomatoes_score', 'double'))
client.send(AddItemProperty('metacritic_score', 'double'))
client.send(AddItemProperty('netflix_release_date', 'timestamp'))
client.send(AddItemProperty('tags', 'set'))