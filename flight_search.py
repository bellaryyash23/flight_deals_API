import os
import requests
from datetime import datetime, timedelta

FLIGHT_API = os.environ.get('FLIGHT_API')
FLIGHT_ENDPOINT = os.environ.get('FLIGHT_ENDPOINT')

date_1 = datetime.now().date() + timedelta(days=1)
FROM_DATE = date_1.strftime("%d/%m/%Y")

date_2 = date_1 + timedelta(days=6 * 30)
TO_DATE = date_2.strftime("%d/%m/%Y")

headers = {
    "apikey": FLIGHT_API,
}


class FlightSearch:

    def __init__(self):
        self.flight_price = []
        self.flight_dates = []
        self.flight_dates_return = []
        self.city_names = []

    def get_flight_prices(self, iata_codes):
        for code in iata_codes:
            parameters = {
                "fly_from": f"{code}",
                "fly_to": "LHR",
                "date_from": f"{FROM_DATE}",
                "date_to": f"{TO_DATE}",
                "one_for_city": 1,
            }
            response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=parameters)
            response.raise_for_status()
            try:
                self.flight_price.append(response.json()["data"][0]["price"])
                self.flight_dates.append(response.json()["data"][0]["route"][0]["local_arrival"].split("T")[0])
                self.flight_dates_return.append(response.json()["data"][0]["route"][1]["local_arrival"].split("T")[0])
                self.city_names.append(response.json()["data"][0]["route"][0]["cityFrom"])
            except IndexError:
                self.flight_price.append(0)
                self.flight_dates.append(0)
                self.flight_dates_return.append(0)
                self.city_names.append(0)
        return self.flight_price

    def get_flight_dates(self):
        return self.flight_dates

    def get_return_flight_dates(self):
        return self.flight_dates_return

    def get_city_name(self):
        return self.city_names
