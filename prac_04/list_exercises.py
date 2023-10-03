"""CP1404 Practical 04 List Exercises Questions"""


def main():
    # Part 1
    numbers = get_numbers()
    number_information(numbers)
    # Part 2
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    check_username(usernames)

# Part 1
def get_numbers():
    """Gets 5 numbers from the user and stores them in a list"""
    numbers = []
    for i in range(5):
        valid_input = False
        while not valid_input:
            try:
                number = int(input("Number: "))
                numbers.append(number)
                valid_input = True
            except ValueError:
                print("Invalid Entry")
    return numbers


def number_information(numbers):
    """Prints information about a list of numbers"""
    print(f"The first number is: {numbers[0]}")
    print(f"The last number is: {numbers[-1]}")
    print(f"The smallest number is: {min(numbers)}")
    print(f"The largest number is: {max(numbers)}")
    print(f"The average of the numbers is: {sum(numbers) / len(numbers):.2f}")


# Part 2
def check_username(usernames):
    """Checks if a users username is in a list of allowed usernames"""
    username = input("Enter your user name: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()
