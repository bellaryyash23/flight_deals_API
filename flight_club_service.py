import os
import requests
# https://replit.com/@YashBellary1/flightclubservice#main.py

SHEET_USER_ENDPOINT = os.environ.get('SHEET_USER_ENDPOINT')

print("Welcome to Yash Flight Club.")
print("We find best flight deals and email you.")

vaild_details = True

while vaild_details:
    f_name = input("What is your first name ?\n").title()
    l_name = input("What is your last name ?\n").title()
    email = input("Enter your email address: \n")
    confirm_email = input("Please confirm your email address: \n")
    if email == confirm_email:
        print("Congratulation, you are in the Club.")
        break
    else:
        print("Please Check your details and re-enter again.")

user_details = {
  "user": {
    "firstName": f_name,
    "lastName": l_name,
    "email": email
  }
}

response = requests.post(url=SHEET_USER_ENDPOINT, json=user_details)
response.raise_for_status()
print(response.text)
