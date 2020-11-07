import os
import json
import requests
import secrets
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from yelp.client import Client

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
        self.club_ratings = self.get_club_ratings()
        self.save_as_parquet(self.club_ratings)

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
        return results

    def save_as_parquet(selfs, club_ratings):
        df = pd.DataFrame(club_ratings)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, 'test.parquet')


if __name__ == '__main__':
    ratings = GetRatings()
