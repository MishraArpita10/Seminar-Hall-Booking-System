# maintenance.py
from datetime import datetime
from hallManagement import halls, view_halls, get_hall_by_id

# In-memory list of maintenance dictionaries
maintenance_records = []

# Valid status options stored as a tuple
VALID_STATUSES = ("Scheduled", "In Progress", "Completed")


# Helper to find a hall by numeric ID or exact/partial name
def find_hall(hall_input):
    hall_input = hall_input.strip()
    if hall_input.isdigit():
        return get_hall_by_id(int(hall_input))

    for hall in halls:
        if hall["name"].strip().lower() == hall_input.lower():
            return hall
    return None


# Check whether a hall has an active/planned maintenance conflict
def check_maintenance_conflict(hall_id, maint_date, start_time, end_time):
    for record in maintenance_records:
        # Completed maintenance no longer blocks the hall
        if record["status"] == "Completed":
            continue

        if record["hall_id"] == hall_id and record["date_obj"] == maint_date:
            if start_time < record["end_obj"] and record["start_obj"] < end_time:
                return True
    return False


# 1. Schedule / Log Hall Maintenance
def schedule_maintenance():
    print("\n========== SCHEDULE HALL MAINTENANCE ==========")
    view_halls()

    hall_input = input("\nEnter Hall ID or Hall Name: ").strip()
    hall = find_hall(hall_input)

    if hall is None:
        print("Hall not found.")
        return

    task_type = input("Enter maintenance type (e.g., Projector Repair, AC Servicing, Deep Cleaning): ").strip()
    if not task_type:
        print("Maintenance type cannot be empty.")
        return

    date_str = input("Enter maintenance date (DD-MM-YYYY): ").strip()
    start_str = input("Enter start time (HH:MM): ").strip()
    end_str = input("Enter end time (HH:MM): ").strip()

    try:
        maint_date = datetime.strptime(date_str, "%d-%m-%Y").date()
        start_time = datetime.strptime(start_str, "%H:%M").time()
        end_time = datetime.strptime(end_str, "%H:%M").time()
    except ValueError:
        print("Invalid date or time format. Use DD-MM-YYYY and HH:MM (24-hour).")
        return

    if start_time >= end_time:
        print("End time must be after start time.")
        return

    print("\nSelect Initial Status:")
    print("1. Scheduled")
    print("2. In Progress")
    print("3. Completed")
    status_choice = input("Enter choice (1-3, default 1): ").strip()

    if status_choice == "2":
        status = "In Progress"
    elif status_choice == "3":
        status = "Completed"
    else:
        status = "Scheduled"

    # Check if maintenance overlaps with an existing maintenance window
    if status != "Completed" and check_maintenance_conflict(hall["hall_id"], maint_date, start_time, end_time):
        print(f"Conflict! {hall['name']} already has maintenance scheduled during this time.")
        return

    # Check if maintenance overlaps with an existing event booking
    from booking_management import bookings
    for booking in bookings:
        if booking["hall_id"] == hall["hall_id"] and booking["date_obj"] == maint_date:
            if start_time < booking["end_obj"] and booking["start_obj"] < end_time:
                print(
                    f"Conflict! {hall['name']} is booked for '{booking['event_name']}' "
                    f"({booking['start']} to {booking['end']}) on {booking['date']}."
                )
                return

    new_id = max((r["maintenance_id"] for r in maintenance_records), default=0) + 1

    record = {
        "maintenance_id": new_id,
        "hall_id": hall["hall_id"],
        "hall_name": hall["name"],
        "task_type": task_type.title(),
        "date": maint_date.strftime("%d-%m-%Y"),
        "start": start_time.strftime("%H:%M"),
        "end": end_time.strftime("%H:%M"),
        "date_obj": maint_date,
        "start_obj": start_time,
        "end_obj": end_time,
        "status": status
    }

    maintenance_records.append(record)

    print("\n========== MAINTENANCE LOGGED ==========")
    print("Maintenance ID :", record["maintenance_id"])
    print("Hall           :", f"{record['hall_name']} (ID: {record['hall_id']})")
    print("Task / Issue   :", record["task_type"])
    print("Date           :", record["date"])
    print("Time Window    :", f"{record['start']} to {record['end']}")
    print("Status         :", record["status"])
    print("========================================")


# 2. View Maintenance Schedule (with optional filter by hall or status)
def view_maintenance_logs():
    if not maintenance_records:
        print("\nNo maintenance records found.")
        return

    print("\nFilter Maintenance Logs:")
    print("1. View All")
    print("2. Filter by Hall (ID or Name)")
    print("3. Filter by Status")
    filter_choice = input("Enter choice (1-3, default 1): ").strip()

    filtered = maintenance_records

    if filter_choice == "2":
        hall_query = input("Enter Hall ID or Name: ").strip()
        hall = find_hall(hall_query)
        if hall is None:
            print("Hall not found.")
            return
        filtered = [r for r in maintenance_records if r["hall_id"] == hall["hall_id"]]

    elif filter_choice == "3":
        status_query = input("Enter status (Scheduled / In Progress / Completed): ").strip().lower()
        filtered = [r for r in maintenance_records if r["status"].lower() == status_query]

    if not filtered:
        print("\nNo matching maintenance records found.")
        return

    print("\n=======================================================================================")
    print(f"{'ID':<4} | {'Hall':<18} | {'Issue / Task':<20} | {'Date':<10} | {'Time Window':<13} | {'Status'}")
    print("---------------------------------------------------------------------------------------")
    for r in filtered:
        time_window = f"{r['start']}-{r['end']}"
        print(
            f"{r['maintenance_id']:<4} | {r['hall_name']:<18} | {r['task_type']:<20} | "
            f"{r['date']:<10} | {time_window:<13} | {r['status']}"
        )
    print("=======================================================================================")


# 3. Update Maintenance Status
def update_maintenance_status():
    if not maintenance_records:
        print("\nNo maintenance records available to update.")
        return

    view_maintenance_logs()

    try:
        maint_id = int(input("\nEnter Maintenance ID to update: "))
    except ValueError:
        print("Invalid Maintenance ID.")
        return

    target_record = None
    for record in maintenance_records:
        if record["maintenance_id"] == maint_id:
            target_record = record
            break

    if target_record is None:
        print("Maintenance ID not found.")
        return

    print(f"\nCurrent Status for ID {maint_id} ({target_record['hall_name']} - {target_record['task_type']}): {target_record['status']}")
    print("Select New Status:")
    print("1. Scheduled")
    print("2. In Progress")
    print("3. Completed")

    choice = input("Enter choice (1-3): ").strip()
    status_map = {
        "1": "Scheduled",
        "2": "In Progress",
        "3": "Completed"
    }

    if choice not in status_map:
        print("Invalid status selection.")
        return

    new_status = status_map[choice]

    # Re-check conflict if reopening a Completed task to Scheduled/In Progress
    if target_record["status"] == "Completed" and new_status != "Completed":
        if check_maintenance_conflict(
            target_record["hall_id"],
            target_record["date_obj"],
            target_record["start_obj"],
            target_record["end_obj"]
        ):
            print("Cannot reopen: another active maintenance task overlaps this time slot.")
            return

    target_record["status"] = new_status
    print(f"\nMaintenance ID {maint_id} status updated to '{new_status}'.")


# 4. Cancel / Remove Maintenance Entry
def cancel_maintenance():
    if not maintenance_records:
        print("\nNo maintenance records available to cancel.")
        return

    view_maintenance_logs()

    try:
        maint_id = int(input("\nEnter Maintenance ID to cancel/remove: "))
    except ValueError:
        print("Invalid Maintenance ID.")
        return

    for record in maintenance_records:
        if record["maintenance_id"] == maint_id:
            maintenance_records.remove(record)
            print(
                f"\nMaintenance ID {maint_id} ({record['hall_name']} - {record['task_type']}) "
                "removed. Time window is now free."
            )
            return

    print("Maintenance ID not found.")


# 5. Check Hall Operational Readiness
def check_hall_readiness():
    if not halls:
        print("\nNo halls available in the system.")
        return

    print("\n========== CHECK HALL OPERATIONAL READINESS ==========")
    date_str = input("Enter date to check (DD-MM-YYYY): ").strip()
    start_str = input("Enter start time (HH:MM): ").strip()
    end_str = input("Enter end time (HH:MM): ").strip()

    try:
        check_date = datetime.strptime(date_str, "%d-%m-%Y").date()
        start_time = datetime.strptime(start_str, "%H:%M").time()
        end_time = datetime.strptime(end_str, "%H:%M").time()
    except ValueError:
        print("Invalid date or time format. Use DD-MM-YYYY and HH:MM (24-hour).")
        return

    if start_time >= end_time:
        print("End time must be after start time.")
        return

    from booking_management import check_availability

    print(f"\nHall Status on {date_str} ({start_str} to {end_str}):")
    print("------------------------------------------------------------------")
    print(f"{'ID':<4} | {'Hall Name':<20} | {'Capacity':<10} | {'Operational Status'}")
    print("------------------------------------------------------------------")

    for hall in halls:
        under_maint = check_maintenance_conflict(hall["hall_id"], check_date, start_time, end_time)
        is_free_from_booking = check_availability(hall["hall_id"], check_date, start_time, end_time)

        if under_maint:
            status = "Under Maintenance"
        elif not is_free_from_booking:
            status = "Booked"
        else:
            status = "Ready"

        print(f"{hall['hall_id']:<4} | {hall['name']:<20} | {hall['capacity']:<10} | {status}")

    print("------------------------------------------------------------------")