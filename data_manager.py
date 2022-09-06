import os

import requests

SHEET_ENDPOINT = os.environ.get('SHEET_ENDPOINT')

SHEET_USER_ENDPOINT = os.environ.get('SHEET_USER_ENDPOINT')

headers = {
    "authorization": "Bearer Secure@007"
}


class DataManager:

    def __init__(self):
        self.user_data = []
        self.city_data = []
        self.price_data = []
        self.get_city_data()

    def get_city_data(self):   # To get data from PRICES sheet
        response = requests.get(url=SHEET_ENDPOINT)
        response.raise_for_status()
        self.city_data = response.json()["prices"]
        return self.city_data

    def update_iata_codes(self, iata_codes):
        i = 2
        for code in iata_codes:
            row_data = {
                "price": {
                    "iataCode": f"{code}"
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{i}", json=row_data)
            response.raise_for_status()
            i += 1

    def get_max_price(self):
        self.price_data = [data["lowestPrice"] for data in self.city_data]
        return self.price_data

    def get_user_data(self):
        response = requests.get(url=SHEET_USER_ENDPOINT)
        response.raise_for_status()
        self.user_data = response.json()["users"]
        return self.user_data
