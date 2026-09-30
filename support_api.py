# Customer Support API Automation
# This project retrieves customer information from an API
# and displays selected customer details.

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(API_URL)

if response.status_code == 200:
    customers = response.json()

    print("Customer Support Information")
    print("----------------------------")

    for customer in customers[:5]:
        print(f"Name: {customer['name']}")
        print(f"Email: {customer['email']}")
        print(f"Company: {customer['company']['name']}")
        print("----------------------------")

else:
    print("Unable to retrieve customer information.")
    print(f"Status code: {response.status_code}")
