# Travel Planner App

A console-based Travel Planner application built with Python using Object-Oriented Programming.

## Features

- **User Management** - Register and login with unique username/email checks and encrypted password storage
- **Trip Management** - Create and view trips with destination and travel dates
- **Hotel Booking** - Add hotel bookings to a selected trip with nightly cost and number of nights
- **Activity Planning** - Add trip activities with date and cost
- **Budget Tracking** - View total spending summary (hotels + activities) for each trip
- **Destination Discovery** - Browse a built-in destination list that also grows as users add new trip destinations

## User Flow

1. Register or login from the guest menu.
2. Create one or more trips.
3. Add hotels and activities to a selected trip.
4. Track trip budget totals at any time.
5. Logout or exit the app.

## How to Run

```bash
python main.py
```

## Project Structure

```text
Travel_Page/
|- main.py      # Menu-driven console application
|- travel.py    # OOP models: User, Trip, Hotel, Activity
|- README.md
```

## Notes

- Data is stored in memory only while the app is running.
- Passwords use a simple character-shift encryption for learning purposes, not production security.
