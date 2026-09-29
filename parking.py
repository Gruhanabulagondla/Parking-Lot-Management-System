from datetime import datetime

parking = {}
MAX_SLOTS = 5
RATE_PER_HOUR = 20


def park_vehicle():
    if len(parking) >= MAX_SLOTS:
        print("\nParking lot is full!")
        return

    vehicle_number = input("\nEnter vehicle number: ").upper()

    if vehicle_number in parking:
        print("Vehicle is already parked.")
        return

    parking[vehicle_number] = datetime.now()

    print("Vehicle parked successfully.")
    print(f"Available slots: {MAX_SLOTS - len(parking)}")


def remove_vehicle():
    vehicle_number = input("\nEnter vehicle number: ").upper()

    if vehicle_number not in parking:
        print("Vehicle not found.")
        return

    entry_time = parking[vehicle_number]
    exit_time = datetime.now()

    seconds = (exit_time - entry_time).total_seconds()
    hours = max(1, int(seconds // 3600))

    fee = hours * RATE_PER_HOUR

    del parking[vehicle_number]

    print("\n========== PARKING BILL ==========")
    print("Vehicle:", vehicle_number)
    print("Parking Hours:", hours)
    print(f"Parking Fee: ₹{fee}")
    print("Vehicle removed successfully.")


def view_vehicles():
    print("\n========== PARKED VEHICLES ==========")

    if not parking:
        print("No vehicles parked.")
        return

    for vehicle, time in parking.items():
        print(f"{vehicle} - Entry: {time.strftime('%H:%M:%S')}")


def main():
    print("========== PARKING LOT MANAGEMENT ==========")

    while True:
        print("\n1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. View Parked Vehicles")
        print("4. View Available Slots")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            park_vehicle()

        elif choice == "2":
            remove_vehicle()

        elif choice == "3":
            view_vehicles()

        elif choice == "4":
            print(
                f"\nAvailable Slots: {MAX_SLOTS - len(parking)}/{MAX_SLOTS}"
            )

        elif choice == "5":
            print("\nThank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()