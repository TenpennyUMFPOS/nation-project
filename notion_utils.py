import requests
from config import HEADERS

def get_database_properties(database_id):
    url = f"https://api.notion.com/v1/databases/{database_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
