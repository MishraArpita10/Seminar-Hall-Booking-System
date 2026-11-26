

from datetime import date, time
from booking_management import bookings, cancel_booking, check_availability
from unittest.mock import patch
from booking_management import book_hall

# Save existing bookings
original_bookings = bookings.copy()

# Clear list only for isolated testing
bookings.clear()

# Add temporary test booking
test_booking = {
    "booking_id": 999,
    "hall_id": 1,
    "date_obj": date(2026, 12, 10),
    "start_obj": time(10, 0),
    "end_obj": time(12, 0)
}

bookings.append(test_booking)


# TEST 1: Overlapping booking
result1 = check_availability(
    1, date(2026, 12, 10), time(11, 0), time(13, 0)
)
print("Test 1 - Overlapping booking:",
      "PASS" if not result1 else "FAIL")


# TEST 2: Non-overlapping booking
result2 = check_availability(
    1, date(2026, 12, 10), time(12, 0), time(14, 0)
)
print("Test 2 - Non-overlapping booking:",
      "PASS" if result2 else "FAIL")


# TEST 3: Different hall, same time
result3 = check_availability(
    2, date(2026, 12, 10), time(10, 0), time(12, 0)
)
print("Test 3 - Different hall, same time:",
      "PASS" if result3 else "FAIL")


# TEST 4: Same hall, different date
result4 = check_availability(
    1, date(2026, 12, 11), time(10, 0), time(12, 0)
)
print("Test 4 - Same hall, different date:",
      "PASS" if result4 else "FAIL")


# TEST 5: Exact duplicate booking
result5 = check_availability(
    1, date(2026, 12, 10), time(10, 0), time(12, 0)
)
print("Test 5 - Exact duplicate booking:",
      "PASS" if not result5 else "FAIL")


# Restore original bookings AFTER ALL TESTS
bookings[:] = original_bookings

print("\nAll booking tests completed!")

# TEST 6: Zero attendees
with patch("builtins.input", side_effect=[
    "Alankriti",          # Organizer
    "Python Seminar",     # Event
    "1",                  # Hall ID
    "0"                   # Attendees
]):
    print("\nTEST 6: Zero attendees")
    book_hall()


# TEST 7: Negative attendees
with patch("builtins.input", side_effect=[
    "Alankriti",
    "Python Seminar",
    "1",
    "-5"
]):
    print("\nTEST 7: Negative attendees")
    book_hall()


# TEST 8: Invalid Hall ID
with patch("builtins.input", side_effect=[
    "Alankriti",
    "Python Seminar",
    "999"
]):
    print("\nTEST 8: Invalid Hall ID")
    book_hall()



# TEST 9: Past booking date
with patch("builtins.input", side_effect=[
    "Alankriti",
    "Python Seminar",
    "1",
    "50",
    "01-01-2020",
    "10:00",
    "12:00"
]):
    print("\nTEST 9: Past booking date")
    book_hall()


# TEST 10: Invalid date format
with patch("builtins.input", side_effect=[
    "Alankriti",
    "Python Seminar",
    "1",
    "50",
    "2026/12/10",
    "10:00",
    "12:00"
]):
    print("\nTEST 10: Invalid date format")
    book_hall()


# TEST 11: Start time equals end time
with patch("builtins.input", side_effect=[
    "Alankriti",
    "Python Seminar",
    "1",
    "50",
    "10-12-2026",
    "10:00",
    "10:00"
]):
    print("\nTEST 11: Equal start and end time")
    book_hall()



# TEST 12: Start time later than end time
with patch("builtins.input", side_effect=[
    "Alankriti",
    "Python Seminar",
    "1",
    "50",
    "10-12-2026",
    "14:00",
    "12:00"
]):
    print("\nTEST 12: Start time later than end time")
    book_hall()


# TEST 13: Overlapping booking through book_hall()
with patch("builtins.input", side_effect=[
    "Alankriti",
    "Python Seminar",
    "1",
    "50",
    "10-12-2026",
    "11:00",
    "13:00"
]):
    print("\nTEST 13: Overlapping booking")
    book_hall()


# TEST 14: Cancel a non-existing booking
with patch("builtins.input", side_effect=["9999"]):
    print("\nTEST 14: Cancel non-existing booking")
    cancel_booking()
