from datetime import datetime


class User:
    _next_user_id = 1
    used_emails = set()
    used_usernames = set()

    def __init__(self, username, email, password):
        if username in User.used_usernames:
            print("Username already exists.")
            return
        if email in User.used_emails:
            print("Email already registered.")
            return

        self._user_id = User._next_user_id
        User._next_user_id += 1

        self.username = username
        self.email = email
        self._password = self._encrypt_password(password)
        self.is_logged_in = False

        self.trips = {}

        User.used_usernames.add(username)
        User.used_emails.add(email)

        print(f"User '{username}' registered successfully.")

    def _encrypt_password(self, password):
        encrypted = ""
        for ch in password:
            encrypted += chr(ord(ch) + 3)
        return encrypted

    def _check_password(self, password):
        return self._password == self._encrypt_password(password)

    def login(self, password):
        if self.is_logged_in:
            print("You are already logged in.")
            return True

        if self._check_password(password):
            self.is_logged_in = True
            print(f"Welcome, {self.username}!")
            return True

        print("Wrong password.")
        return False

    def logout(self):
        if not self.is_logged_in:
            print("You are not logged in.")
            return
        self.is_logged_in = False
        print("Logged out.")

    def add_trip(self, name, destination, start_date, end_date):
        trip_id = len(self.trips) + 1
        trip = Trip(trip_id, name, destination, start_date, end_date)
        self.trips[trip_id] = trip
        print(f"Trip '{name}' created successfully.")
        return trip

    def display_trips(self):
        if len(self.trips) == 0:
            print("You have no trips")
            return

        print(f"\n{self.username}'s Trips")
        header = f"{'ID':<5} {'Name':<20} {'Destination':<20}"
        print(header)

        for trip in self.trips.values():
            row = f"{trip._trip_id:<5} {trip.name:<20} {trip.destination:<20}"
            print(row)
        print()


class Trip:
    def __init__(self, trip_id, name, destination, start_date, end_date):
        self._trip_id = trip_id
        self.name = name
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.hotels = []
        self.activities = []

    def add_hotel(self, name, price_per_night, number_of_nights, location):
        hotel = Hotel(name, price_per_night, number_of_nights,location)
        self.hotels.append(hotel)
        print(f"Hotel '{name}' added successfully.")

    def add_activity(self, name, cost, date):
        activity = Activity(name, cost, date)
        self.activities.append(activity)
        print(f"Activity '{name}' added successfully.")

    def display_budget(self):
        hotel_cost = sum(h.total_price for h in self.hotels)
        activities_cost = sum(a.cost for a in self.activities)

        print(f"\nBudget for: {self.name}")
        print(f"Hotels: ${hotel_cost:.2f}")
        print(f"Activities: ${activities_cost:.2f}")
        print(f"Total: ${hotel_cost + activities_cost:.2f}")


class Hotel:
    def __init__(self, name, price_per_night, number_of_nights,location):
        self.name = name
        self.price_per_night = price_per_night
        self.location = location
        self.number_of_nights = number_of_nights
        self.total_price = price_per_night * number_of_nights


class Activity:
    def __init__(self, name, cost, date):
        self.name = name
        self.cost = cost
        self.date = date