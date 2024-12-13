from Flight import Flight
from Trip import Trip
from Booking import Booking

def main():
    # Создание рейсов
    flight1 = Flight("AA123", "New York", "Los Angeles", "2023-10-01 10:00", "2023-10-01 13:00", 100)
    flight2 = Flight("AA124", "New York", "Chicago", "2023-10-01 14:00", "2023-10-01 16:00", 50)
    
    # Создание путешествия
    trip = Trip()
    trip.add_flight(flight1)
    trip.add_flight(flight2)

    # Создание бронирования
    booking_system = Booking()
    if booking_system.create_booking(flight1):
        print(f"Бронирование на рейс {flight1.flight_number} успешно.")
    else:
        print(f"Нет доступных мест на рейс {flight1.flight_number}.")

    if booking_system.create_booking(flight2):
        print(f"Бронирование на рейс {flight2.flight_number} успешно.")
    else:
        print(f"Нет доступных мест на рейс {flight2.flight_number}.")

    # Проверка доступности мест
    print(f"Доступные места на рейс {flight1.flight_number}: {flight1.available_seats()}")
    print(f"Доступные места на рейс {flight2.flight_number}: {flight2.available_seats()}")

if __name__ == "__main__":
    main()