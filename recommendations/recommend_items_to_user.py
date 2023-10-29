from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
import json

client = RecombeeClient(
    'lab01-movies',
    '4n1qnl6MbwhopsLr61jV8uxK3jnYBHswPJV8OV7Qg5vzd5ezJ2vezjZ7fYmjIiAl',
    region=Region.EU_WEST
)

user = "user-27"

recommended = client.send(RecommendItemsToUser(user, 10))
print(recommended)

with open(f"../resources/recommended-{user}.json", "w") as json_file:
    json.dump(recommended, json_file, indent=4)