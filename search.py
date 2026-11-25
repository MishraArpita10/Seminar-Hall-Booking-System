# Import hall data from Hall Management module

from hallManagement import halls
from booking_management import bookings
from datetime import datetime

# Search hall using Hall ID
def search_hall_by_id(hall_id):

    for hall in halls:

        if hall["hall_id"] == hall_id:
            return hall

    return None



# Search hall using its name
def search_hall_by_name(name):

    name = name.strip().lower()

    results = []

    for hall in halls:

        if name in hall["name"].lower():
            results.append(hall)

    return results


# Search halls using minimum capacity
def search_hall_by_capacity(min_capacity):

    results = []

    for hall in halls:

        if hall["capacity"] >= min_capacity:
            results.append(hall)

    return results


# Search halls based on available equipment
def search_hall_by_equipment(equipment_name):

    equipment_name = equipment_name.strip().lower()

    if not equipment_name:
        return []

    results = []

    for hall in halls:

        for equipment in hall["equipment"]:

            if equipment_name == equipment.lower():
                results.append(hall)
                break

    return results


def search_booking_by_id(booking_id):

    for booking in bookings:

        if booking["booking_id"] == booking_id:
            return [booking]

    return []

def search_booking_by_organizer(name):

    name = name.strip().lower()
    results = []

    for booking in bookings:

        if name in booking["organizer"].lower():
            results.append(booking)

    return results

def search_bookings_by_hall_id(hall_id):

    results = []

    for booking in bookings:

        if booking["hall_id"] == hall_id:
            results.append(booking)

    return results

def search_bookings_by_date(booking_date):

    results = []

    for booking in bookings:

        if booking["date"] == booking_date:
            results.append(booking)

    return results


def display_results(results):

    if not results:
        print("\nNo matching halls found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for hall in results:
        print("\nHall ID:", hall["hall_id"])
        print("Hall Name:", hall["name"])
        print("Capacity:", hall["capacity"])
        print("Equipment:", ", ".join(hall["equipment"]))

    print("====================================")




# Search halls using capacity and equipment together
def search_hall_by_criteria(min_capacity, equipment_name):

    equipment_name = equipment_name.strip().lower()
    if not equipment_name:
        return []
    results = []

    for hall in halls:

        # Check minimum capacity
        if hall["capacity"] >= min_capacity:

            # Check whether required equipment exists
            for equipment in hall["equipment"]:

                if equipment.lower() == equipment_name:
                    results.append(hall)
                    break

    return results


def display_booking_results(results):

    if not results:
        print("\nNo matching bookings found.")
        return

    print("\n========== BOOKING SEARCH RESULTS ==========")

    for booking in results:

        print("\nBooking ID:", booking["booking_id"])
        print("Organizer:", booking["organizer"])
        print("Event:", booking["event_name"])
        print("Hall:", booking["hall_name"])
        print("Hall ID:", booking["hall_id"])
        print("Attendees:", booking["attendees"])
        print("Date:", booking["date"])
        print("Time:", booking["start"], "to", booking["end"])

    print("\n============================================")


# Search Menu
def search_menu():

    while True:

        
        print("\n========== SEARCH MENU ==========")
        print("1. Search Hall by ID")
        print("2. Search Hall by Name")
        print("3. Search Hall by Capacity")
        print("4. Search Hall by Equipment")
        print("5. Search by Multiple Criteria")
        print("6. Search Booking by ID")
        print("7. Search Booking by Organizer")
        print("8. Search Bookings by Hall ID")
        print("9. Search Bookings by Date")
        print("10. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            try:
                hall_id = int(input("Enter Hall ID: "))

                if hall_id <= 0:
                    print("Hall ID must be positive.")
                    continue

                hall = search_hall_by_id(hall_id)

                if hall:
                    display_results([hall])
                else:
                    print("Hall not found.")

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":

            name = input("Enter Hall Name: ").strip()

            if not name:
                print("Hall name cannot be empty.")
                continue

            results = search_hall_by_name(name)
            display_results(results)

        elif choice == "3":

            try:
                capacity = int(input("Enter minimum capacity: "))

                if capacity <= 0:
                    print("Capacity must be positive.")
                    continue

                results = search_hall_by_capacity(capacity)
                display_results(results)

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "4":
            equipment = input("Enter required equipment: ").strip()

            if not equipment:
                print("Equipment name cannot be empty.")
                continue

            results = search_hall_by_equipment(equipment)
            display_results(results)

        elif choice == "5":
            try:
                capacity = int(input("Enter minimum capacity: "))
                equipment = input("Enter required equipment: ").strip()
                if capacity <= 0:
                    print("Capacity must be positive.")
                    continue
                elif not equipment:
                    print("Equipment name cannot be empty.")
                    continue
                else:
                    results = search_hall_by_criteria(capacity, equipment)
                    display_results(results)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "6":
            try:
                booking_id = int(input("Enter Booking ID: "))

                if booking_id <= 0:
                    print("Booking ID must be positive.")
                    continue

                results = search_booking_by_id(booking_id)
                display_booking_results(results)

            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "7":
            organizer_name = input("Enter Organizer Name: ").strip()
            if not organizer_name:
                print("Organizer name cannot be empty.")
                continue
            results = search_booking_by_organizer(organizer_name)
            display_booking_results(results)
        elif choice == "8": 
            try:
                hall_id = int(input("Enter Hall ID: "))

                if hall_id <= 0:
                    print("Hall ID must be positive.")
                    continue

                results = search_bookings_by_hall_id(hall_id)
                display_booking_results(results)

            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "9":
            date_str = input("Enter Booking Date (YYYY-MM-DD): ").strip()
            try:
                booking_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                results = search_bookings_by_date(booking_date)
                display_booking_results(results)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")    
        elif choice == "10":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    search_menu()






