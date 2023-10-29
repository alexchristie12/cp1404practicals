"""CP1404 Guitars Exercise"""

from prac_06.guitar import Guitar


def main():
    """Program that stores a list of Guitar and their details."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    if name == "":
        return
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar = Guitar(name, year, cost)
    print(f"{name} ({year}) : ${cost:.2f} added.")
    guitars.append(new_guitar)
    while name != "":
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage(2023):
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year:>4}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
