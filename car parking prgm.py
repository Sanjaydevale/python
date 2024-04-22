class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity

    def park_car(self):
        if self.available_spaces > 0:
            print("Car parked successfully.")
            self.available_spaces -= 1
        else:
            print("Parking lot is full. Car cannot be parked.")

    def leave_car(self):
        if self.available_spaces < self.capacity:
            print("Car exited successfully.")
            self.available_spaces += 1
        else:
            print("Parking lot is already empty. No car to exit.")


def main():
    capacity = 50  # Define the capacity of the parking lot
    parking_lot = ParkingLot(capacity)

    while True:
        print("\n1. Park Car")
        print("2. Leave Car")
        print("3. Check Available Spaces")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            parking_lot.park_car()
        elif choice == '2':
            parking_lot.leave_car()
        elif choice == '3':
            print(f"Available spaces: {parking_lot.available_spaces}")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
