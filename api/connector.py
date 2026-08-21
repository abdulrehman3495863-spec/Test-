import requests
import json

class APIConnector:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {api_key}'} if api_key else {}

    def fetch_data(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", 
                                headers=self.headers, 
                                params=params)
        response.raise_for_status()
        return response.json()
