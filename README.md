# Seminar Hall Booking System

## Project Overview
The Seminar Hall Booking System is a Python-based application designed to manage seminar hall bookings efficiently. It allows users to view available halls, search for halls, make bookings, view existing bookings, and cancel bookings.

## Features

### 1. Hall Management
- View all available seminar halls.
- Add new halls.
- Delete existing halls.
- View hall details such as capacity and equipment.

### 2. Booking Management
- Book a seminar hall.
- Check hall availability for a selected date and time.
- Prevent overlapping bookings.
- Validate attendee capacity.
- View all bookings.
- Cancel bookings using Booking ID.

### 3. Search Management
- Search halls by Hall ID.
- Search halls by name.
- Search halls by minimum capacity.
- Search halls by equipment.
- Search halls using multiple criteria.
- Search bookings by Booking ID.
- Search bookings by organizer name.
- Search bookings by Hall ID.
- Search bookings by booking date.

## Technologies Used
- Python
- Git and GitHub
- VS Code

## Project Structure

```text
Seminar-Hall-Booking-System/
│
├── main.py
├── hallManagement.py
├── bookingManagement.py
├── search.py
└── README.md
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/MishraArpita10/Seminar-Hall-Booking-System.git
```

2. Navigate to the project directory:

```bash
cd Seminar-Hall-Booking-System
```

3. Run the application:

```bash
python main.py
```

## Modules

| File | Responsibility |
|---|---|
| `main.py` | Main menu and integration |
| `hallManagement.py` | Hall-related operations |
| `bookingManagement.py` | Booking and cancellation operations |
| `search.py` | Hall and booking search operations |

## Contributors

Developed as a group academic project.

## Future Enhancements
- Database integration for permanent data storage.
- User authentication.
- Booking history and reports.
- Improved user interface.
