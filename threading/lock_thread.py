"""
Problem Statement:
You are designing a ticket booking system where multiple users can book seats at the same time. 
However, since multiple threads might attempt to modify the available seats simultaneously, there is a risk of overbooking. 
Implement a locking mechanism to ensure that seats are booked correctly.


"""


import threading
import time

class TicketBooking:
    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.lock = threading.Lock()  # Lock to manage concurrent booking

    def book_ticket(self, seats_requested):
        with self.lock:  # Ensure one thread at a time modifies available seats
            if self.available_seats >= seats_requested:
                print(f"{threading.current_thread().name} booked {seats_requested} seat(s).")
                self.available_seats -= seats_requested
            else:
                print(f"{threading.current_thread().name} tried to book {seats_requested} seat(s), but not enough seats available.")

# Initialize ticket booking system with 5 available seats
booking_system = TicketBooking(5)

# Define booking requests from different threads
def try_booking(seats):
    booking_system.book_ticket(seats)

# Create multiple user threads
t1 = threading.Thread(target=try_booking, args=(3,), name="User 1")
t2 = threading.Thread(target=try_booking, args=(2,), name="User 2")
t3 = threading.Thread(target=try_booking, args=(2,), name="User 3")  # This may fail due to seat shortage

# Start all booking requests
t1.start()
t2.start()
t3.start()

# Ensure all threads complete
t1.join()
t2.join()
t3.join()

print(f"Final available seats: {booking_system.available_seats}")