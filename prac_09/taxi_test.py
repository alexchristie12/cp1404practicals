"""
CP1404 Practical 09 - Taxi Exercise
Estimated Time: 10 minutes
Actual Time: 
"""

from taxi import Taxi


def main():
    """Main Program for taxi testing program"""
    # Initialise Taxi
    my_taxi = Taxi("Prius 1", 100, 1.23)
    # Drive the Taxi 40km
    my_taxi.drive(40)
    print(my_taxi)
    # Start a new fare and drive 100km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


if __name__ == "__main__":
    main()
