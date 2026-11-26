# Seminar Hall Booking System

A Python-based, menu-driven Seminar Hall Booking System that allows users to manage seminar halls, create and manage bookings, check hall availability, and search for halls and bookings.

## 1. Project Overview

The Seminar Hall Booking System is developed using Python. It provides a simple, interactive, console-based interface through which users can manage halls and bookings efficiently.

The system is divided into independent modules to make the code organised, reusable, and easier to maintain.

## 2. Features

### Hall Management
- View all available seminar halls.
- Add new seminar halls.
- Delete existing halls.
- Assign hall IDs automatically.
- Validate hall names to prevent duplicate hall entries.
- Store hall capacity and available equipment.

### Booking Management
- Book a seminar hall for an event.
- View all existing bookings.
- Cancel an existing booking.
- Validate organizer and event details.
- Validate attendee count against hall capacity.
- Validate booking date and time.
- Prevent bookings for past dates and invalid time slots.
- Generate unique booking IDs.

### Hall Availability and Duplicate Booking Prevention
- Check whether a hall is available for a selected date and time.
- Prevent two bookings from overlapping in the same hall.
- Allow bookings in different halls at the same time.
- Allow adjacent bookings when one booking ends exactly when another begins.

### Search Module
Users can search using the following criteria:

**Hall Search**
- Search hall by ID.
- Search hall by name.
- Search halls by minimum capacity.
- Search halls by equipment.
- Search using multiple criteria (capacity and equipment).

**Booking Search**
- Search booking by ID.
- Search bookings by organizer.
- Search bookings by hall ID.
- Search bookings by date.

## 3. Technologies Used

- **Programming Language:** Python
- **Date and Time Handling:** Python `datetime` module
- **Testing:** Python test scripts
- **Version Control:** Git and GitHub
- **Development Environment:** Visual Studio
