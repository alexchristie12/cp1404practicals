"""CP1404 Practical 07 Guitar Exercise.
Time Estimate : 10 minutes
Actual Time : 9 minutes
"""
from guitar import Guitar


def main():
    """Reads Guitar data and store it in Guitar objects."""
    guitars = []
    # Read the File
    with open("guitars.csv", 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    # Add in new guitars, should go until blank name is entered
    name = input("Enter guitars name: ")
    while name != "":
        year = int(input("Enter guitar's year: "))
        value = float(input("Enter guitar's value: "))
        new_guitar = Guitar(name, year, value)
        guitars.append(new_guitar)
        name = input("Enter guitars name: ")
    # Write Guitar objects to the csv file
    guitars.sort()
    with open("guitars.csv", 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
