from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
import json

client = RecombeeClient(
  'lab01-movies',
  '4n1qnl6MbwhopsLr61jV8uxK3jnYBHswPJV8OV7Qg5vzd5ezJ2vezjZ7fYmjIiAl',
  region=Region.EU_WEST
)

# Set item values
requests = []

with open('../resources/movies.json') as f:
    data = json.loads(f.read())
    for item_id, values in data.items():
        r = SetItemValues(item_id,
                          values,
                          cascade_create=True)
        requests.append(r)

res = client.send(Batch(requests))
