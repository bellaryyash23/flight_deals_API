from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Initialize the classes from imports
flightcode_data = FlightData()
datasheet_manager = DataManager()
flightprice_data = FlightSearch()
notification_manager = NotificationManager()
# ---------------------------------------------- #

# GET city data from PRICES sheets
city_data = datasheet_manager.get_city_data()

# GET user data from USERS sheet
user_data = datasheet_manager.get_user_data()

# IATA code list from flight search using city names
iata_codes = flightcode_data.get_iata_code(city_data)

# UPDATE IATA codes in PRICES sheet
datasheet_manager.update_iata_codes(iata_codes)

# GET Maximum price from given PRICES sheet in list form
price_data = datasheet_manager.get_max_price()

# GET current flight prices from flight search in list form
flight_price_data = flightprice_data.get_flight_prices(iata_codes)

# GET flight dates first departure dates
flight_date_data = flightprice_data.get_flight_dates()

# GET next return dates
flight_date_return = flightprice_data.get_return_flight_dates()

# GET city name of destination
city_name = flightprice_data.get_city_name()

# Use compare method from notification_manager to check Max prices and Current prices
# and store their indexes in a list in that file
comparison = notification_manager.compare(price_data, flight_price_data)

# Send Message using Twilio passing required fields to format the message
notification_manager.send_message(iata_codes, flight_date_data, flight_date_return, city_name)

# Send Email to users registered from Replit and USER sheet pass required fields to format message
notification_manager.send_email(iata_codes, flight_date_data, flight_date_return, city_name, user_data)
