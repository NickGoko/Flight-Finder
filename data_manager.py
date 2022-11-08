import requests
# from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/39e2a8a4a6946ffd8bb9e5dfb1742f8a/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_endpoint = SHEETY_PRICES_ENDPOINT
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f" {SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            return response.json()


