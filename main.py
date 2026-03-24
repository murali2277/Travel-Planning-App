from travel import User


def show_title():
    print("TRAVEL PLANNER APP")


def show_guest_menu():
    print("\nGuest Menu")
    print("1. Register")
    print("2. Login")
    print("0. Exit")


def show_user_menu(username):
    print(f"\n{username}'s Menu")
    print("1. Create Trip")
    print("2. View Trips")
    print("3. Book Hotel")
    print("4. Add Activity")
    print("5. Track Budget")
    print("6. Search Destinations")
    print("7. Logout")
    print("0. Exit")


def read_number(prompt=">> "):
    user_input = input(prompt).strip()
    if user_input.isdigit():
        return int(user_input)
    return -1


class TravelApp:
    def __init__(self):
        self.all_users = {}
        self.current_user = None
        self.destinations = {"India","Paris", "Tokyo", "New York", "Dubai"}

    def register_user(self):
        print("\nRegister")
        username = input("Username: ").strip()
        email = input("Email: ").strip()
        password = input("Password: ").strip()

        if username == "" or email == "" or password == "":
            print("All fields are required.")
            return

        if username in User.used_usernames:
            print("Username already exists.")
            return

        if email in User.used_emails:
            print("Email already registered.")
            return

        new_user = User(username, email, password)
        self.all_users[username] = new_user

    def login_user(self):
        print("\nLogin")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username not in self.all_users:
            print("User not found. Please register first.")
            return

        selected_user = self.all_users[username]
        if selected_user.login(password):
            self.current_user = selected_user

    def create_trip(self):
        if not self.current_user.is_logged_in:
            print("Please login first.")
            return

        print("\nCreate Trip")
        name = input("Trip name: ").strip()
        destination = input("Destination: ").strip()
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()

        if name == "" or destination == "" or start_date == "" or end_date == "":
            print("All fields are required.")
            return
        self.destinations.add(destination)
        self.current_user.add_trip(name, destination, start_date, end_date)

    def view_trips(self):
        if not self.current_user.is_logged_in:
            print("Please login first.")
            return

        self.current_user.display_trips()

    def book_hotel(self):
        if not self.current_user.is_logged_in:
            print("Please login first.")
            return

        if len(self.current_user.trips) == 0:
            print("No trips. Create a trip first.")
            return

        self.current_user.display_trips()
        trip_id = read_number("Enter trip ID: ")

        trip = None
        for t in self.current_user.trips.values():
            if t._trip_id == trip_id:
                trip = t
                break

        if not trip:
            print("Trip not found.")
            return

        print("\nBook Hotel")
        hotel_name = input("Hotel name: ").strip()
        number_of_nights = int(input("Number of nights: "))
        price = input("Price per night: ").strip()
        location = input("Location: ").strip()

        if hotel_name == "" or price == "" or location == "" or number_of_nights <= 0:
            print("All fields are required.")
            return
        price = float(price)
        trip.add_hotel(hotel_name, price, number_of_nights,location)

    def add_activity(self):
        if not self.current_user.is_logged_in:
            print("Please login first.")
            return

        if len(self.current_user.trips) == 0:
            print("No trips. Create a trip first.")
            return

        self.current_user.display_trips()
        trip_id = read_number("Enter trip ID: ")

        trip = None
        for t in self.current_user.trips.values():
            if t._trip_id == trip_id:
                trip = t
                break

        if not trip:
            print("Trip not found.")
            return

        print("\nAdd Activity")
        activity_name = input("Activity name: ").strip()
        cost = input("Cost: ").strip()
        date = input("Date (YYYY-MM-DD): ").strip()

        if activity_name == "" or cost == "" or date == "":
            print("All fields are required.")
            return
        cost = float(cost)
        trip.add_activity(activity_name, cost, date)

    def track_budget(self):
        if not self.current_user.is_logged_in:
            print("Please login first.")
            return

        if len(self.current_user.trips) == 0:
            print("No trips to track.")
            return

        self.current_user.display_trips()
        trip_id = read_number("Enter trip ID: ")

        trip = None
        for t in self.current_user.trips.values():
            if t._trip_id == trip_id:
                trip = t
                break

        if not trip:
            print("Trip not found.")
            return
        trip.display_budget()

    def search_destinations(self):
        print("\nDestinations")
        for i, dest in enumerate(self.destinations, 1):
            print(f"{i}. {dest}")

    def logout_user(self):
        self.current_user.logout()
        self.current_user = None

    def run(self):
        show_title()

        while True:
            if self.current_user is None:
                show_guest_menu()
                choice = read_number()

                if choice == 1:
                    self.register_user()
                elif choice == 2:
                    self.login_user()
                elif choice == 0:
                    print("\nGoodbye!")
                    break
                else:
                    print("Please choose a valid option.")
            else:
                show_user_menu(self.current_user.username)
                choice = read_number()

                if choice == 1:
                    self.create_trip()
                elif choice == 2:
                    self.view_trips()
                elif choice == 3:
                    self.book_hotel()
                elif choice == 4:
                    self.add_activity()
                elif choice == 5:
                    self.track_budget()
                elif choice == 6:
                    self.search_destinations()
                elif choice == 7:
                    self.logout_user()
                elif choice == 0:
                    print("\nGoodbye!")
                    break
                else:
                    print("Please choose a valid option.")


if __name__ == "__main__":
    app = TravelApp()
    app.run()
