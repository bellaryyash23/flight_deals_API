# ✈Flight Deals Club using Requests API of Python

🌟A program which sends registered users discounted flight deals alert of the next 6 months from the data present in a Google sheet via email and SMS which they
can use to avail the offers.

🌟The program makes use of APIs like Sheety API(https://sheety.co/) for reading & updating data from Google Sheets, Tequila API by Kiwi.com(https://tequila.kiwi.com/portal/login)
to get data regarding Flight prices/Airport details, Twilio API(https://www.twilio.com/) for sending SMS on mobile numbers and SMTP module to send mail to users.

👉The Flight Deals Club's user registration portal is a python file 'flight_club_service.py' which, uses Sheety API to add user details to the User 
Registration Google sheet. The program is hosted on replit which makes accessing the portal simple for new registration.

![Replit User Registration Portal](https://github.com/bellaryyash23/flight_deals_API/blob/master/samples/replit_service.jpg?raw=true)

👆Replit User Registration Portal👆

👉The Registered users data is added and stored in the Google Sheet which is updated using Sheety API.

![Registered User's Google Sheet](https://github.com/bellaryyash23/flight_deals_API/blob/master/samples/user_sheet.jpg?raw=true)

👆Registered User's Google Sheet👆

👉After the user registration process is completed the backend of program is executed. 

👉First the flight and destination details along with the maximum flight price values is acquired from the predefined Google Sheet. This is done in the 'data_manger.py'
file. 

![Flight Prices Google Sheet](https://github.com/bellaryyash23/flight_deals_API/blob/master/samples/deals_sheet.jpg?raw=true)

👆Flight Prices Data Google Sheet👆

👉Next, the Kiwi API is used to get values of flight price of the next 6 month and this price is compared with the cutoff flight prices acquired from above sheet. The
API call and present flight price acquisition is done in the 'flight_search.py' file. 

👉This returned data contains all important datafields like return date, flight airport IATA codes and departure date. All these values along with flight price are 
appended to respective lists for future reference.

👉After that, the data of registered users is acquired into the program for data utilization and implementing the alert sending process in later part of program.

👉Now, the data acquired from API call i.e. the flight prices are compared with the cutoff flight prices from the previously acquired data from the predefined Google sheet.
If the prices are less than their cutoff values then the process of sending alerts is triggered. 

👉The Twilio API is used for sending SMS alerts to user's registered mobile number. This is done using the user data acquired previously. The message is formated using 
all the datafields respesctive lists and it is then sent to user alerting them about the discount.

![Mobile SMS Alert](https://github.com/bellaryyash23/flight_deals_API/blob/master/samples/mobile.jpeg?raw=true)

👆Mobile SMS Alert👆

👉The SMTP module is used to send email to the users registered mail id. Just like in the case of Twilio, here also the data is formated using previously acquired data
and along with this format a Google Flights link is also attached additionally for the user to instantly view & avail the offer.
All these tasks of message formating and message sending are carried out in the 'notification_manager.py' file.

![Mail Alert](https://github.com/bellaryyash23/flight_deals_API/blob/master/samples/mail.jpg?raw=true)

👆Mail Alert👆

🌟In this way using various API calls and their methods the Flight Deals Club program is implemented.
