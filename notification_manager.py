import os
import smtplib
from twilio.rest import Client

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

MY_EMAIL = os.environ.get('EMAIL')
MY_PASSWORD = "Secure@007"


class NotificationManager:

    def __init__(self):
        self.max_price = []
        self.present_price = []
        self.indexes = []

    def compare(self, prices, flight_price):
        self.max_price = prices
        self.present_price = flight_price
        for i in range(0, len(prices)):
            if flight_price[i] == 0:  # Because flight is not available so no use.
                print("Something Wrong")
            elif prices[i] > flight_price[i]:
                self.indexes.append(i)

    def send_message(self, iata_codes, dates, return_dates, city_names):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        for i in self.indexes:
            message = client.messages \
                .create(
                body=f"\nLow price alert! Only ${self.present_price[i]}, to fly to {city_names[i]}-{iata_codes[i]} "
                     f"from LONDON-LHR, from {dates[i]} to {return_dates[i]}",
                from_='+12675441487',
                to=os.environ.get('NUMBER')
            )
            print(message.status)

    def send_email(self, iata_codes, dates, return_dates, city_names, user_data):
        connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for user in user_data:  # Itter through the users list first
            for i in self.indexes:  # Check all flight deals from list
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=f"{user['email']}",
                                    msg=f"Subject:New Low Price Flight\n\n"
                                        f"Hello {user['firstName']},\nLow price alert! Only ${self.present_price[i]}, "
                                        f"to fly to {city_names[i]}-{iata_codes[i]} from LONDON-LHR, from {dates[i]} to"
                                        f" to {return_dates[i]}.\n\nGoogle flight link for the flight is "
                                        f"https://www.google.co.uk/flights?hl=en#flt={iata_codes[i]}.LHR.{dates[i]}*"
                                        f"{iata_codes[i]}.LHR.{return_dates[i]}\n\nThank You.")
