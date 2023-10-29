from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
import json
import random
from datetime import datetime, timedelta

client = RecombeeClient(
    'lab01-movies',
    '4n1qnl6MbwhopsLr61jV8uxK3jnYBHswPJV8OV7Qg5vzd5ezJ2vezjZ7fYmjIiAl',
    region=Region.EU_WEST
)

# Function to utils random timestamps within a date range
def random_timestamp(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)
    return start_date + timedelta(days=random_days, seconds=random_seconds)

# List of user IDs and item IDs
user_ids = ['user-' + str(i) for i in range(1, 201)]
item_ids = client.send(ListItems())

# Generate detail views data
detail_views = []
start_date = datetime(2016, 4, 20, 0, 0, 0)
end_date = datetime(2016, 4, 21, 0, 0, 0)

for _ in range(2000):
    user_id = random.choice(user_ids)
    item_id = random.choice(item_ids)
    timestamp = random_timestamp(start_date, end_date).isoformat()
    detail_views.append({"user_id": user_id, "item_id": item_id, "timestamp": timestamp})

# Save the detail views data to a JSON file
with open("../resources/detail_views.json", "w") as json_file:
    json.dump(detail_views, json_file, indent=4)

print("detail_views.json has been created.")