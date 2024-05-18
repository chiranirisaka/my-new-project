class Bus:
    def __init__(self, bus_id, capacity):
        self.bus_id = bus_id
        self.capacity = capacity
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.capacity:
            self.booked_seats += 1
            return True
        return False

    def get_available_seats(self):
        return self.capacity - self.booked_seats

    def __str__(self):
        return f"Bus ID: {self.bus_id}, Capacity: {self.capacity}, Booked Seats: {self.booked_seats}"
