from datetime import datetime
from hallManagement import view_halls, get_hall_by_id

# List to store all bookings
bookings = []


# Check whether a hall is available using date and time objects
def check_availability(hall_id, booking_date, start_time, end_time):
    for booking in bookings:
        if booking["hall_id"] == hall_id and booking["date_obj"] == booking_date:
            # Overlap occurs if new start is before existing end AND existing start is before new end
            if start_time < booking["end_obj"] and booking["start_obj"] < end_time:
                return False
    return True


# Book a seminar hall
def book_hall():
    print("\n========== BOOK A SEMINAR HALL ==========")

    organizer = input("Enter organizer name: ").strip()
    event_name = input("Enter event name: ").strip()

    if not organizer or not event_name:
        print("Organizer name and event name cannot be empty.")
        return

    # Show all halls from hallManagement.py
    view_halls()

    try:
        hall_id = int(input("\nEnter Hall ID: "))
    except ValueError:
        print("Invalid Hall ID.")
        return

    hall = get_hall_by_id(hall_id)

    if hall is None:
        print("Hall not found.")
        return

    # Check attendee count against hall capacity
    try:
        attendees = int(input(f"Enter expected attendees (Max {hall['capacity']}): "))
        if attendees <= 0:
            print("Number of attendees must be greater than zero.")
            return
    except ValueError:
        print("Invalid number of attendees.")
        return

    if attendees > hall["capacity"]:
        print(f"Sorry! {hall['name']} has a maximum capacity of {hall['capacity']} people.")
        return

    date = input("Enter booking date (DD-MM-YYYY): ").strip()
    start = input("Enter start time (HH:MM): ").strip()
    end = input("Enter end time (HH:MM): ").strip()

    # Validate date and time format
    try:
        booking_date = datetime.strptime(date, "%d-%m-%Y").date()
        start_time = datetime.strptime(start, "%H:%M").time()
        end_time = datetime.strptime(end, "%H:%M").time()
    except ValueError:
        print("Invalid date or time format. Use DD-MM-YYYY and HH:MM (24-hour).")
        return

    # Check past date
    if booking_date < datetime.today().date():
        print("Cannot book a hall for a past date.")
        return

    # Check if booking is today and start time has already passed
    if booking_date == datetime.today().date() and start_time <= datetime.now().time():
        print("Cannot book a hall for a time that has already passed today.")
        return

    # Check start vs end time
    if start_time >= end_time:
        print("End time must be after start time.")
        return

    # Check availability
    if not check_availability(hall_id, booking_date, start_time, end_time):
        print(f"Sorry! {hall['name']} is already booked during this time.")
        return

    # Generate unique booking ID (safe even after deletions)
    new_booking_id = max((b["booking_id"] for b in bookings), default=0) + 1

    formatted_date = booking_date.strftime("%d-%m-%Y")
    formatted_start = start_time.strftime("%H:%M")
    formatted_end = end_time.strftime("%H:%M")

    # Create booking record
    booking = {
        "booking_id": new_booking_id,
        "organizer": organizer,
        "event_name": event_name,
        "attendees": attendees,
        "hall_id": hall_id,
        "hall_name": hall["name"],
        "equipment": hall["equipment"],
        "date": formatted_date,
        "start": formatted_start,
        "end": formatted_end,
        "date_obj": booking_date,
        "start_obj": start_time,
        "end_obj": end_time
    }

    bookings.append(booking)

    # Display confirmation
    print("\n========== BOOKING SUCCESSFUL ==========")
    print("Booking ID:", booking["booking_id"])
    print("Organizer:", organizer)
    print("Event:", event_name)
    print("Attendees:", f"{attendees} / {hall['capacity']}")
    print("Hall:", hall["name"])
    print("Included Equipment:", ", ".join(hall["equipment"]))
    print("Date:", formatted_date)
    print("Time:", formatted_start, "to", formatted_end)
    print("========================================")


# View all bookings
def view_bookings():
    if not bookings:
        print("\nNo bookings have been made yet.")
        return

    print("\n========== ALL BOOKINGS ==========")

    for booking in bookings:
        print("\nBooking ID:", booking["booking_id"])
        print("Organizer:", booking["organizer"])
        print("Event:", booking["event_name"])
        print("Attendees:", booking["attendees"])
        print("Hall:", booking["hall_name"])
        print("Date:", booking["date"])
        print("Time:", booking["start"], "to", booking["end"])

    print("\n==================================")


# Cancel a booking by Booking ID
def cancel_booking():
    if not bookings:
        print("\nNo bookings available to cancel.")
        return

    view_bookings()

    try:
        booking_id = int(input("\nEnter Booking ID to cancel: "))
    except ValueError:
        print("Invalid Booking ID.")
        return

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            bookings.remove(booking)
            print(f"\nBooking ID {booking_id} ({booking['event_name']}) cancelled successfully!")
            return

    print("\nBooking ID not found.")



