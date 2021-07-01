class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)

print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Kev", "Tom", "Jason", "Maddie"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} to flight")
    else:
        print(f"No available seats for {person}")

