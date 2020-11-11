import json
import secrets
import requests
from yelp.client import Client
from python.shared.methods import save_as_parquet

nba_cities = [
    'Atlanta',
    'Boston',
    'Brooklyn',
    'Charlotte',
    'Chicago',
    'Cleveland',
    'Dallas',
    'Denver',
    'Detroit',
    'Houston',
    'Indiana',
    'Los Angeles',
    'Memphis',
    'Miami',
    'Milwaukee',
    'Minnesota',
    'New Orleans',
    'New York',
    'Oklahoma City',
    'Orlando',
    'Philadelphia',
    'Phoenix',
    'Portland',
    'Sacramento',
    'San Antonio',
    'San Francisco',
    'Toronto',
    'Utah',
    'Washington'
]


class GetRatings:
    def __init__(self):
        self.url = 'https://api.yelp.com/v3/businesses/search'
        self.client = self.get_yelp_client()
        self.get_club_ratings()

    def get_yelp_client(self):
        client = Client(secrets.api_key)
        return client

    def get_club_ratings(self):
        results = []
        headers = {'Authorization': 'Bearer %s' % secrets.api_key}
        for city in nba_cities:
            parameters = {'term': 'Strip Club', 'location': city}
            request = requests.get(self.url, params=parameters, headers=headers)
            if (request.status_code != 400):
                request_json = json.loads(request.text)
                results.extend(request_json['businesses'])
        save_as_parquet(results, 'stripClubRatings')


if __name__ == '__main__':
    ratings = GetRatings()
