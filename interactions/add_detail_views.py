from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
import json

client = RecombeeClient(
    'lab01-movies',
    '4n1qnl6MbwhopsLr61jV8uxK3jnYBHswPJV8OV7Qg5vzd5ezJ2vezjZ7fYmjIiAl',
    region=Region.EU_WEST
)

requests = []

with open('../resources/detail_views.json') as f:
    interactions = json.loads(f.read())
    for interaction in interactions:
        r = AddDetailView(interaction['user_id'],
                          interaction['item_id'],
                          timestamp=interaction['timestamp'],
                          cascade_create=True)
        requests.append(r)

br = Batch(requests)
client.send(br)
