from datetime import datetime

class Flight:
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, arrival_time, total_seats):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = datetime.strptime(departure_time, "%Y-%m-%d %H:%M")
        self.arrival_time = datetime.strptime(arrival_time, "%Y-%m-%d %H:%M")
        self.total_seats = total_seats
        self.booked_seats = 0

    def duration(self):
        return self.arrival_time - self.departure_time

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False