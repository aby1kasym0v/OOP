class Trip:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        if not self.check_time_conflict(flight):
            self.flights.append(flight)
            return True
        return False

    def check_time_conflict(self, new_flight):
        for flight in self.flights:
            if (new_flight.departure_time < flight.arrival_time and
                new_flight.arrival_time > flight.departure_time):
                return True
        return False

    def get_flights(self):
        return self.flights