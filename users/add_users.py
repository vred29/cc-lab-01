from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *

client = RecombeeClient(
    'lab01-movies',
    '4n1qnl6MbwhopsLr61jV8uxK3jnYBHswPJV8OV7Qg5vzd5ezJ2vezjZ7fYmjIiAl',
    region=Region.EU_WEST
)

for i in range(1, 201):
    user_id = f'user-{i}'
    client.send(AddUser(user_id))

print("200 users have been added.")
