from datetime import datetime, timedelta

 # datetime.now() + timedelta(months=6)
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.departure_airport_code =origin_airport
        self.departure_city = origin_city
        self.destination_city = destination_city
        self.out_date = out_date
        self.return_date = return_date
