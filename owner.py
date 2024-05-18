from bus import Bus

class Owner:
    def __init__(self):
        self.buses = []

    def add_bus(self, bus_id, capacity):
        bus = Bus(bus_id, capacity)
        self.buses.append(bus)
        print(f"Bus {bus_id} added with capacity {capacity}.")

    def view_buses(self):
        for bus in self.buses:
            print(bus)
