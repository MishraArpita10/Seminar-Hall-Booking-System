
print("Welcome to Seminar Hall Booking System!")

from hallManagement import (
    view_halls,
    add_hall,
    delete_hall,
    get_hall_by_id,
    search_hall_by_name,
    update_hall,
    sort_halls_by_capacity,
    count_halls
)

from booking_management import (
    book_hall,
    view_bookings,
    cancel_booking
)

from search import search_menu


# ==========================================
# HALL MANAGEMENT MENU
# ==========================================

def hall_management_menu():

    while True:
        print("\n========== HALL MANAGEMENT ==========")
        print("1. View All Halls")
        print("2. Add Hall")
        print("3. Update Hall Details")
        print("4. Delete Hall")
        print("5. Search Hall by Name")
        print("6. View Hall by ID")
        print("7. Sort Halls by Capacity")
        print("8. Count Total Halls")
        print("9. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_halls()

        elif choice == "2":
            name = input("Enter Hall Name: ").strip()

            try:
                capacity = int(input("Enter Hall Capacity: "))

                equipment_input = input(
                    "Enter equipment separated by commas: "
                )

                equipment = equipment_input.split(",")

                add_hall(name, capacity, equipment)

            except ValueError:
                print("Please enter a valid capacity.")

        elif choice == "3":
            try:
                hall_id = int(input("Enter Hall ID to update: "))

                hall = get_hall_by_id(hall_id)

                if hall is None:
                    print("Hall not found.")
                    continue

                print("\nLeave a field blank to keep its current value.")

                print(f"Current Name: {hall['name']}")
                new_name = input("Enter new name: ").strip()

                print(f"Current Capacity: {hall['capacity']}")
                capacity_input = input("Enter new capacity: ").strip()

                print(f"Current Equipment: {', '.join(hall['equipment'])}")
                equipment_input = input(
                    "Enter new equipment separated by commas: "
                ).strip()

                new_capacity = None
                new_equipment = None

                if capacity_input:
                    new_capacity = int(capacity_input)

                if equipment_input:
                    new_equipment = equipment_input.split(",")

                update_hall(
                    hall_id,
                    name=new_name if new_name else None,
                    capacity=new_capacity,
                    equipment=new_equipment
                )

            except ValueError:
                print("Please enter a valid capacity or Hall ID.")

        elif choice == "4":
            try:
                hall_id = int(input("Enter Hall ID to delete: "))
                delete_hall(hall_id)

            except ValueError:
                print("Please enter a valid Hall ID.")

        elif choice == "5":
            name = input("Enter Hall Name to search: ").strip()
            search_hall_by_name(name)

        elif choice == "6":
            try:
                hall_id = int(input("Enter Hall ID: "))
                hall = get_hall_by_id(hall_id)

                if hall:
                    print("\nHall Details:")
                    print(f"ID: {hall['hall_id']}")
                    print(f"Name: {hall['name']}")
                    print(f"Capacity: {hall['capacity']}")
                    print(f"Equipment: {', '.join(hall['equipment'])}")
                else:
                    print("Hall not found.")

            except ValueError:
                print("Please enter a valid Hall ID.")

        elif choice == "7":
            sort_halls_by_capacity()

        elif choice == "8":
            count_halls()

        elif choice == "9":
            break

        else:
            print("Invalid choice! Please try again.")


# ==========================================
# BOOKING MANAGEMENT MENU
# ==========================================

def booking_management_menu():

    while True:
        print("\n========== BOOKING MANAGEMENT ==========")
        print("1. Book a Hall")
        print("2. View Bookings")
        print("3. Cancel Booking")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            book_hall()

        elif choice == "2":
            view_bookings()

        elif choice == "3":
            cancel_booking()

        elif choice == "4":
            break

        else:
            print("Invalid choice! Please try again.")


# ==========================================
# MAIN MENU
# ==========================================

def main_menu():

    while True:
        print("\n========================================")
        print("       SEMINAR HALL BOOKING SYSTEM")
        print("========================================")
        print("1. Hall Management")
        print("2. Booking Management")
        print("3. Search Halls")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            hall_management_menu()

        elif choice == "2":
            booking_management_menu()

        elif choice == "3":
            search_menu()

        elif choice == "4":
            print("\nThank you for using Seminar Hall Booking System!")
            break

        else:
            print("Invalid choice. Please try again.")


# ==========================================
# PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    main_menu()
