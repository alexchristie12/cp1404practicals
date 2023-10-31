"""CP1404 Guitar Class Test"""

from prac_06.guitar import Guitar


def main():
    """Tests that the Guitar class works correctly"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    ibanez = Guitar("Ibanez RGA42FM", 2016, 750)
    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age(2023)}")
    print(f"{ibanez.name} get_age() - Expected 7. Got {ibanez.get_age(2023)}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(2023)}")
    print(f"{ibanez.name} is_vintage() - Expected False. Got {ibanez.is_vintage(2023)}")


if __name__ == "__main__":
    main()
