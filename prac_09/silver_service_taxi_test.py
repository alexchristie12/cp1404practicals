"""
CP1404 Practical 09 - Silver Service Taxi Test
Estimated Time:
Actual Time:
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Testing and verifying the Silver Service Taxi class"""
    test_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    test_taxi.drive(18)
    print(test_taxi)
    assert test_taxi.get_fare() == 48.78


if __name__ == "__main__":
    main()
