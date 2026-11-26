print("Hello this is my main file")
# function to add two numbers 



from hallManagement import view_halls, add_hall, delete_hall
from booking_management import book_hall, view_bookings, cancel_booking
from search import search_menu


def hall_management_menu():

    while True:
        print("\n========== HALL MANAGEMENT ==========")
        print("1. View Halls")
        print("2. Add Hall")
        print("3. Delete Hall")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

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
                hall_id = int(input("Enter Hall ID to delete: "))
                delete_hall(hall_id)

            except ValueError:
                print("Please enter a valid Hall ID.")

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


def booking_management_menu():

    while True:
        print("\n========== BOOKING MANAGEMENT ==========")
        print("1. Book a Hall")
        print("2. View Bookings")
        print("3. Cancel Booking")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_hall()

        elif choice == "2":
            view_bookings()

        elif choice == "3":
            cancel_booking()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


def main_menu():

    while True:
        print("\n========================================")
        print("       SEMINAR HALL BOOKING SYSTEM")
        print("========================================")
        print("1. Hall Management")
        print("2. Booking Management")
        print("3. Search")
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
            
        



if __name__ == "__main__":
    main_menu()
