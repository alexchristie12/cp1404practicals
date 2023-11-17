"""
CP1404 Practical 09 - Taxi Simulator Exercise
Estimated Time: 60 minutes
Actual Time: 80 minutes
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """
    Taxi Service Simulator where the User can:
    - Choose a taxi from a list of available taxis.
    - Choose how far they want to drive
    - Quit the Simulator where it will display the total trip cost
    """

    # Initialise the available taxis
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    current_taxi = None
    total_fare = 0
    print("Lets Drive")
    print_menu()
    # Handle the menu
    menu_choice = input(">>> ")
    while menu_choice.lower() != "q":
        # Handle each option
        if menu_choice == "c":
            current_taxi = choose_taxi(taxis)
        elif menu_choice == "d":
            total_fare = drive_taxi(current_taxi, total_fare)
        else:
            print("Invalid Input")
        menu_choice = input(">>> ")
    # Handle the User quitting
    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def print_menu() -> None:
    print("q)uit, c)hoose, d)rive")


def choose_taxi(taxis: list):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    valid_input = False
    while not valid_input:
        try:
            taxi_number = int(input("Choose Taxi: "))
            new_taxi = taxis[taxi_number]
            valid_input = True
            return new_taxi
        except ValueError:
            print("Invalid Input")
        except IndexError:
            print("Invalid Taxi Choice")


def drive_taxi(current_taxi, total_fare):
    if current_taxi is None:
        print("You need to chosse a taxi before you drive")
    else:
        try:
            current_taxi.start_fare()
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            print(current_taxi.get_fare())
            total_fare += current_taxi.get_fare()
            print(
                f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}"
            )
            print(f"Bill to date: {total_fare}")
            return total_fare

        except ValueError:
            print("Invalid distance input")


if __name__ == "__main__":
    main()
