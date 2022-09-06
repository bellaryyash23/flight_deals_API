import os

import requests

FLIGHT_API = os.environ.get('FLIGHT_API')
FLIGHT_ENDPOINT = os.environ.get('FLIGHT_ENDPOINT')

headers = {
    "apikey": FLIGHT_API,
}


class FlightData:

    def __init__(self):
        self.iata_codes = []

    def get_iata_code(self, city_data):
        for city in city_data:
            parameters = {
                "term": city["city"],
                "location_types": "airport",
                "limit": 1
            }
            response = requests.get(url=FLIGHT_ENDPOINT, params=parameters, headers=headers)
            response.raise_for_status()
            data = response.json()["locations"]
            code = [air_data["code"] for air_data in data]
            self.iata_codes += code
        return self.iata_codes
