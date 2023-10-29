from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
import json

client = RecombeeClient(
  'lab01-movies',
  '4n1qnl6MbwhopsLr61jV8uxK3jnYBHswPJV8OV7Qg5vzd5ezJ2vezjZ7fYmjIiAl',
  region=Region.EU_WEST
)

# Define a ReQL filter that selects all items
filter = 'true'

# Use DeleteMoreItems with the filter to delete all items
result = client.send(DeleteMoreItems(filter))