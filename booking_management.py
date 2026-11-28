
from datetime import datetime
from hallManagement import view_halls, get_hall_by_id
<<<<<<< HEAD
from maintenance import check_maintenance_conflict
# List to store all bookings
=======

# List to store bookings
>>>>>>> 0d838e7f8524c70400e986c198ce42cb0b882245
bookings = []


# --------------------------------------------------
# CHECK AVAILABILITY
# --------------------------------------------------
def check_availability(hall_id, booking_date, start_time, end_time, exclude_id=None):

    for booking in bookings:

        # Skip the booking being updated
        if booking["booking_id"] == exclude_id:
            continue

        if booking["hall_id"] == hall_id and booking["date_obj"] == booking_date:

            # Check time overlap
            if start_time < booking["end_obj"] and booking["start_obj"] < end_time:
                return False

    return True


# --------------------------------------------------
# DISPLAY A SINGLE BOOKING
# --------------------------------------------------
def display_booking(booking):

    print("\n-----------------------------------")
    print("Booking ID:", booking["booking_id"])
    print("Organizer:", booking["organizer"])
    print("Event:", booking["event_name"])
    print("Attendees:", booking["attendees"])
    print("Hall:", booking["hall_name"])
    print("Date:", booking["date"])
    print("Time:", booking["start"], "to", booking["end"])
    print("Equipment:", ", ".join(booking["equipment"]))
    print("-----------------------------------")


# --------------------------------------------------
# VIEW ALL BOOKINGS
# --------------------------------------------------
def view_bookings():

    if not bookings:
        print("\nNo bookings available.")
        return

    print("\n========== ALL BOOKINGS ==========")

    for booking in bookings:
        display_booking(booking)


# --------------------------------------------------
# ADD BOOKING
# --------------------------------------------------
def book_hall():

    print("\n========== BOOK A SEMINAR HALL ==========")

    organizer = input("Enter organizer name: ").strip()
    event_name = input("Enter event name: ").strip()

    if not organizer or not event_name:
        print("Organizer and event name cannot be empty.")
        return

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

    try:
        attendees = int(input(f"Enter expected attendees (Max {hall['capacity']}): "))

        if attendees <= 0:
            print("Attendees must be greater than zero.")
            return

        if attendees > hall["capacity"]:
            print(f"Hall capacity is only {hall['capacity']}.")
            return

    except ValueError:
        print("Invalid attendee count.")
        return

    date = input("Enter booking date (DD-MM-YYYY): ").strip()
    start = input("Enter start time (HH:MM): ").strip()
    end = input("Enter end time (HH:MM): ").strip()

    try:
        booking_date = datetime.strptime(date, "%d-%m-%Y").date()
        start_time = datetime.strptime(start, "%H:%M").time()
        end_time = datetime.strptime(end, "%H:%M").time()

    except ValueError:
        print("Invalid date/time format.")
        return

    if booking_date < datetime.today().date():
        print("Cannot book a past date.")
        return

    if booking_date == datetime.today().date() and start_time <= datetime.now().time():
        print("This time has already passed.")
        return

    if start_time >= end_time:
        print("End time must be after start time.")
        return

    if not check_availability(hall_id, booking_date, start_time, end_time):
        print("Hall is already booked during this time.")
        return
    # Check availability against existing bookings
    if not check_availability(hall_id, booking_date, start_time, end_time):
        print(f"Sorry! {hall['name']} is already booked during this time.")
        return

<<<<<<< HEAD
    # Check conflict against scheduled/in-progress maintenance
    if check_maintenance_conflict(hall_id, booking_date, start_time, end_time):
        print(f"Sorry! {hall['name']} is under maintenance during this time.")
        return
    
    # Generate unique booking ID (safe even after deletions)
    new_booking_id = max((b["booking_id"] for b in bookings), default=0) + 1
=======
    booking_id = max((b["booking_id"] for b in bookings), default=0) + 1
>>>>>>> 0d838e7f8524c70400e986c198ce42cb0b882245

    booking = {
        "booking_id": booking_id,
        "organizer": organizer,
        "event_name": event_name,
        "attendees": attendees,
        "hall_id": hall_id,
        "hall_name": hall["name"],
        "equipment": hall["equipment"],
        "date": booking_date.strftime("%d-%m-%Y"),
        "start": start_time.strftime("%H:%M"),
        "end": end_time.strftime("%H:%M"),
        "date_obj": booking_date,
        "start_obj": start_time,
        "end_obj": end_time
    }

    bookings.append(booking)

    print("\nBooking successful!")
    display_booking(booking)


# --------------------------------------------------
# SEARCH BOOKING BY ID
# --------------------------------------------------
def search_booking_by_id():

    if not bookings:
        print("\nNo bookings available.")
        return

    try:
        booking_id = int(input("Enter Booking ID: "))
    except ValueError:
        print("Invalid Booking ID.")
        return

    for booking in bookings:

        if booking["booking_id"] == booking_id:
            display_booking(booking)
            return

    print("Booking not found.")


# --------------------------------------------------
# SEARCH BOOKING BY ORGANIZER
# --------------------------------------------------
def search_booking_by_organizer():

    if not bookings:
        print("\nNo bookings available.")
        return

    name = input("Enter organizer name: ").strip().lower()

    if not name:
        print("Organizer name cannot be empty.")
        return

    found = False

    for booking in bookings:

        if name in booking["organizer"].lower():
            display_booking(booking)
            found = True

    if not found:
        print("No bookings found for this organizer.")


# --------------------------------------------------
# UPDATE BOOKING
# --------------------------------------------------
def update_booking():

    if not bookings:
        print("\nNo bookings available to update.")
        return

    view_bookings()

    try:
        booking_id = int(input("\nEnter Booking ID to update: "))
    except ValueError:
        print("Invalid Booking ID.")
        return

    booking = None

    for b in bookings:
        if b["booking_id"] == booking_id:
            booking = b
            break

    if booking is None:
        print("Booking not found.")
        return

    print("\nLeave a field blank to keep its current value.")

    new_organizer = input(f"Organizer [{booking['organizer']}]: ").strip()
    new_event = input(f"Event [{booking['event_name']}]: ").strip()
    new_attendees = input(f"Attendees [{booking['attendees']}]: ").strip()

    if new_organizer:
        booking["organizer"] = new_organizer

    if new_event:
        booking["event_name"] = new_event

    if new_attendees:

        try:
            new_attendees = int(new_attendees)

            hall = get_hall_by_id(booking["hall_id"])

            if new_attendees <= 0 or new_attendees > hall["capacity"]:
                print("Invalid attendee count. Update cancelled.")
                return

            booking["attendees"] = new_attendees

        except ValueError:
            print("Invalid attendee count. Update cancelled.")
            return

    print("\nBooking details updated successfully!")
    display_booking(booking)


# --------------------------------------------------
# CANCEL / DELETE BOOKING
# --------------------------------------------------
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
            print("Booking cancelled successfully!")
            return

    print("Booking not found.")


# --------------------------------------------------
# VIEW BOOKINGS BY HALL
# --------------------------------------------------
def view_bookings_by_hall():

    if not bookings:
        print("\nNo bookings available.")
        return

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

    found = False

    print(f"\n========== BOOKINGS FOR {hall['name']} ==========")

    for booking in bookings:

        if booking["hall_id"] == hall_id:
            display_booking(booking)
            found = True

    if not found:
        print("No bookings found for this hall.")


# --------------------------------------------------
# VIEW UPCOMING BOOKINGS
# --------------------------------------------------
def view_upcoming_bookings():

    today = datetime.today().date()

    upcoming = []

    for booking in bookings:

        if booking["date_obj"] >= today:
            upcoming.append(booking)

    if not upcoming:
        print("\nNo upcoming bookings.")
        return

    upcoming.sort(key=lambda b: (b["date_obj"], b["start_obj"]))

    print("\n========== UPCOMING BOOKINGS ==========")

    for booking in upcoming:
        display_booking(booking)


# --------------------------------------------------
# SORT BOOKINGS BY DATE
# --------------------------------------------------
def sort_bookings_by_date():

    if not bookings:
        print("\nNo bookings available.")
        return

    sorted_bookings = sorted(
        bookings,
        key=lambda b: (b["date_obj"], b["start_obj"])
    )

    print("\n========== BOOKINGS SORTED BY DATE ==========")

    for booking in sorted_bookings:
        display_booking(booking)


# --------------------------------------------------
# COUNT TOTAL BOOKINGS
# --------------------------------------------------
def count_bookings():

    print("\nTotal bookings:", len(bookings))


# --------------------------------------------------
# BOOKING MANAGEMENT MENU
# --------------------------------------------------
def booking_management_menu():

    while True:

        print("\n========== BOOKING MANAGEMENT ==========")
        print("1. View all bookings")
        print("2. Add booking")
        print("3. Update booking")
        print("4. Delete / Cancel booking")
        print("5. Search booking by ID")
        print("6. Search booking by organizer")
        print("7. View bookings by hall")
        print("8. View upcoming bookings")
        print("9. Sort bookings by date")
        print("10. Count total bookings")
        print("11. Back to main menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            view_bookings()

        elif choice == 2:
            book_hall()

        elif choice == 3:
            update_booking()

        elif choice == 4:
            cancel_booking()

        elif choice == 5:
            search_booking_by_id()

        elif choice == 6:
            search_booking_by_organizer()

        elif choice == 7:
            view_bookings_by_hall()

        elif choice == 8:
            view_upcoming_bookings()

        elif choice == 9:
            sort_bookings_by_date()

        elif choice == 10:
            count_bookings()

        elif choice == 11:
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
  booking_management_menu()