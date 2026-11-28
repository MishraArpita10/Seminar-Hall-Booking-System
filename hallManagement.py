
# hallManagement.py

# ----------------------------------
# HALL DATABASE
# ----------------------------------

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
        "equipment": [
            "Projector", "Microphone", "Speakers", "Whiteboard"
        ]
    },
    {
        "hall_id": 4,
        "name": "Lecture Hall",
        "capacity": 75,
        "equipment": ["Projector", "Speakers"]
    }
]


# ----------------------------------
# 1. VIEW ALL HALLS
# ----------------------------------

def view_halls():

    if not halls:
        print("\nNo halls registered.")
        return

    print("\n========== ALL SEMINAR HALLS ==========")

    for hall in halls:
        print(f"\nID: {hall['hall_id']}")
        print(f"Name: {hall['name']}")
        print(f"Capacity: {hall['capacity']}")
        print(f"Equipment: {', '.join(hall['equipment'])}")

    print("\n=======================================")


# ----------------------------------
# 2. ADD A NEW HALL
# ----------------------------------

def add_hall(name, capacity, equipment):

    name = name.strip()

    if not name:
        print("\nHall name cannot be empty.")
        return False

    if not isinstance(capacity, int) or capacity <= 0:
        print("\nCapacity must be a positive integer.")
        return False

    if not equipment:
        print("\nAt least one equipment item is required.")
        return False

    # Prevent duplicate hall names
    for hall in halls:
        if hall["name"].lower() == name.lower():
            print("\nA hall with this name already exists.")
            return False

    clean_equipment = [
        item.strip().title()
        for item in equipment
        if item.strip()
    ]

    if not clean_equipment:
        print("\nPlease enter valid equipment names.")
        return False

    new_id = max(
        (hall["hall_id"] for hall in halls),
        default=0
    ) + 1

    new_hall = {
        "hall_id": new_id,
        "name": name,
        "capacity": capacity,
        "equipment": clean_equipment
    }

    halls.append(new_hall)

    print(f"\n{ name } added successfully!")
    return True


# ----------------------------------
# 3. SEARCH HALL BY ID
# ----------------------------------

def get_hall_by_id(hall_id):

    for hall in halls:
        if hall["hall_id"] == hall_id:
            return hall

    return None


# ----------------------------------
# 4. SEARCH HALL BY NAME
# ----------------------------------

def search_hall_by_name(name):

    results = []

    for hall in halls:
        if name.lower() in hall["name"].lower():
            results.append(hall)

    if results:
        print("\nMatching halls:")

        for hall in results:
            print(
                f"{hall['hall_id']} - {hall['name']} "
                f"({hall['capacity']} people)"
            )
    else:
        print("\nNo matching hall found.")

    return results


# ----------------------------------
# 5. FILTER HALLS BY CAPACITY
# ----------------------------------

def filter_by_capacity(min_capacity):

    results = []

    for hall in halls:
        if hall["capacity"] >= min_capacity:
            results.append(hall)

    return results


# ----------------------------------
# 6. FILTER HALLS BY EQUIPMENT
# ----------------------------------

def filter_by_equipment(required_equipment):

    results = []

    required_equipment = [
        item.strip().lower()
        for item in required_equipment
    ]

    for hall in halls:

        available_equipment = [
            item.lower()
            for item in hall["equipment"]
        ]

        if all(
            item in available_equipment
            for item in required_equipment
        ):
            results.append(hall)

    return results


# ----------------------------------
# 7. UPDATE HALL DETAILS
# ----------------------------------

def update_hall(hall_id, name=None, capacity=None, equipment=None):

    hall = get_hall_by_id(hall_id)

    if hall is None:
        print("\nHall not found.")
        return False

    if name is not None:
        name = name.strip()

        if not name:
            print("\nHall name cannot be empty.")
            return False

        for other_hall in halls:
            if (
                other_hall["hall_id"] != hall_id
                and other_hall["name"].lower() == name.lower()
            ):
                print("\nAnother hall already has this name.")
                return False

        hall["name"] = name

    if capacity is not None:
        if not isinstance(capacity, int) or capacity <= 0:
            print("\nInvalid capacity.")
            return False

        hall["capacity"] = capacity

    if equipment is not None:
        clean_equipment = [
            item.strip().title()
            for item in equipment
            if item.strip()
        ]

        if not clean_equipment:
            print("\nAt least one valid equipment item is required.")
            return False

        hall["equipment"] = clean_equipment

    print("\nHall details updated successfully!")
    return True


# ----------------------------------
# 8. DELETE A HALL
# ----------------------------------

def delete_hall(hall_id):

    hall = get_hall_by_id(hall_id)

    if hall is None:
        print("\nHall not found.")
        return False

    halls.remove(hall)

    print(f"\n{hall['name']} deleted successfully!")
    return True


# ----------------------------------
# 9. SORT HALLS BY CAPACITY
# ----------------------------------

def sort_halls_by_capacity():

    sorted_halls = sorted(
        halls,
        key=lambda hall: hall["capacity"]
    )

    print("\nHalls sorted by capacity:")

    for hall in sorted_halls:
        print(
            f"{hall['name']} - {hall['capacity']} people"
        )

    return sorted_halls


# ----------------------------------
# 10. COUNT TOTAL HALLS
# ----------------------------------

def count_halls():

    total = len(halls)

    print(f"\nTotal registered halls: {total}")

    return total
