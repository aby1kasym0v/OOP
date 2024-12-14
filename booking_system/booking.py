class Booking:
    def __init__(self):
        self.bookings = []

    def create_booking(self, flight):
        if flight.book_seat():
            self.bookings.append(flight)
            return True
        return False

    def check_availability(self, flight):
        return flight.available_seats() > 0