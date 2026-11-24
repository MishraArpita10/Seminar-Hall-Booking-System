
# hallManagement.py

# List to store all seminar hall details
halls = [
    {
        "hall_id": 1,
        "name": "Seminar Hall A",
        "capacity": 100,
        "equipment": ["Projector", "Whiteboard", "Microphone"]
    },
    {
        "hall_id": 2,
        "name": "Seminar Hall B",
        "capacity": 50,
        "equipment": ["Projector", "Whiteboard"]
    },
    {
        "hall_id": 3,
        "name": "Conference Hall",
        "capacity": 200,
        "equipment": ["Projector", "Microphone", "Speakers", "Whiteboard"]
    },
    {
        "hall_id": 4,
        "name": "Lecture Hall",
        "capacity": 75,
        "equipment": ["Projector", "Speakers"]
    }
]


# Display all available halls
def view_halls():
    if not halls:
        print("\nNo halls are available.")
        return

    print("\n========== AVAILABLE HALLS ==========")

    for hall in halls:
        print(f"\nHall ID: {hall['hall_id']}")
        print(f"Hall Name: {hall['name']}")
        print(f"Capacity: {hall['capacity']} people")
        print(f"Equipment: {', '.join(hall['equipment'])}")

    print("\n=====================================")


# Add a new hall
def add_hall(name, capacity, equipment):
    if not name.strip():
        print("Hall name cannot be empty.")
        return False

    if capacity <= 0:
        print("Capacity must be greater than zero.")
        return False

    if not equipment:
        print("Please provide at least one equipment item.")
        return False

    new_id = max(
        (hall["hall_id"] for hall in halls),
        default=0
    ) + 1

    new_hall = {
        "hall_id": new_id,
        "name": name.strip(),
        "capacity": capacity,
        "equipment": [item.strip().title() for item in equipment if item.strip()]
    }

    halls.append(new_hall)

    print(f"\n{new_hall['name']} added successfully!")
    return True


# Find a hall using its ID
def get_hall_by_id(hall_id):
    for hall in halls:
        if hall["hall_id"] == hall_id:
            return hall

    return None


# Delete a hall using its ID
def delete_hall(hall_id):
    hall = get_hall_by_id(hall_id)

    if hall is None:
        print("\nHall not found.")
        return False

    halls.remove(hall)
    print(f"\n{hall['name']} deleted successfully!")
    return True
