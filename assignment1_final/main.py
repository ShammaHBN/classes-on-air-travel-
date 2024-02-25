class Person:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age
    def get_age(self):
        return self.age

    def set_gender(self, gender):
        self.gender = gender
    def get_gender(self):
        return self.gender

    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email


class Passenger(Person):
    def __init__(self, name, age, gender, email, passport_num, seat_num):
        super().__init__(name, age, gender, email)
        self.passport_num = passport_num
        self.seat_num = seat_num

    def set_passport_num(self, passport_num):
        self.passport_num = passport_num
    def get_passport_num(self):
        return self.passport_num

    def set_seat_num(self, seat_num):
        self.seat_num = seat_num
    def get_seat_num(self):
        return self.seat_num

    def book_flight(self):
        pass

    def board_flight(self):
        pass

    def find_seat(self):
        pass


class Ticket:
    def __init__(self, name, seat_number, airlines, city, destination, date, time, terminal, arrival_time):
        self.name = name
        self.seat_number = seat_number
        self.airlines = airlines
        self.city = city
        self.destination = destination
        self.date = date
        self.time = time
        self.terminal = terminal
        self.arrival_time = arrival_time

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_seat_number(self, seat_number):
        self.seat_number = seat_number

    def get_seat_number(self):
        return self.seat_number

    def set_airlines(self, airlines):
        self.airlines = airlines

    def get_airlines(self):
        return self.airlines

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_destination(self, destination):
        self.destination = destination

    def get_destination(self):
        return self.destination

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_terminal(self, terminal):
        self.terminal = terminal

    def get_terminal(self):
        return self.terminal

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_arrival_time(self):
        return self.arrival_time


class Flight:
    def __init__(self, airlines, city, terminal, date, boarding_time, arrival_time):
        self.airlines = airlines
        self.city = city
        self.terminal = terminal
        self.date = date
        self.boarding_time = boarding_time
        self.arrival_time = arrival_time

    def set_airlines(self, airlines):
        self.airlines = airlines

    def get_airlines(self):
        return self.airlines

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_terminal(self, terminal):
        self.terminal = terminal

    def get_terminal(self):
        return self.terminal

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_boarding_time(self, boarding_time):
        self.boarding_time = boarding_time

    def get_boarding_time(self):
        return self.boarding_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_arrival_time(self):
        return self.arrival_time

    def departure(self):
        pass

    def land(self):
        pass


class Airport:
    def __init__(self, airport_name, city, gate):
        self.airport_name = airport_name
        self.city = city
        self.gate = gate

    def set_airport_name(self, airport_name):
        self.airport_name = airport_name

    def get_airport_name(self):
        return self.airport_name

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_gate(self, gate):
        self.gate = gate

    def get_gate(self):
        return self.gate

    def verification_system(self):
        pass

    def security_system(self):
        pass


class Airlines:
    def __init__(self, airlines_name, name, terminal):
        self.airlines_name = airlines_name
        self.name = name
        self.terminal = terminal

    def set_airlines_name(self, airlines_name):
        self.airlines_name = airlines_name

    def get_airlines_name(self):
        return self.airlines_name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_terminal(self, terminal):
        self.terminal = terminal

    def get_terminal(self):
        return self.terminal

    def give_ticket(self):
        pass


# Creating objects of the Person class
# Creating objects of the Person class
person1 = Person("Shamma Hassan", 19, "Female", "Shamma@gmail.com")
person2 = Person("Gwenn Marthena", 25, "Female", "gwenn@example.com")

# Creating objects of the Ticket class
ticket1 = Ticket("Shamma hassan", "A21", "japan airlines", "dubai", "Japan", "2024-03-01", "10:00", "Terminal1", "12:00")
ticket2 = Ticket("Gwenn Marthena", "B28", "fly dubai", "dubai", "Baku", "2024-03-02", "11:00", "Terminal2", "13:00")

# Print information using getters
print("Person 1:")
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Gender:", person1.get_gender())
print("Email:", person1.get_email())

print("\nTicket 1:")
print("Name:", ticket1.get_name())
print("Seat Number:", ticket1.get_seat_number())
print("Airlines:", ticket1.get_airlines())
print("City:", ticket1.get_city())
print("Destination:", ticket1.get_destination())
print("Date:", ticket1.get_date())
print("Time:", ticket1.get_time())
print("Terminal:", ticket1.get_terminal())
print("Arrival Time:", ticket1.get_arrival_time())

print("\nTicket 2:")
print("Name:", ticket2.get_name())
print("Seat Number:", ticket2.get_seat_number())
print("Airlines:", ticket2.get_airlines())
print("City:", ticket2.get_city())
print("Destination:", ticket2.get_destination())
print("Date:", ticket2.get_date())
print("Time:", ticket2.get_time())
print("Terminal:", ticket2.get_terminal())
print("Arrival Time:", ticket2.get_arrival_time())




