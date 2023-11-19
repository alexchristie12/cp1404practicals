"""Password Checking Program"""
MINIMUM_PASSWORD_LENGTH = 6


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter Password: ")
    while len(password) <= MINIMUM_PASSWORD_LENGTH:
        print("Password not long enough!!")
        password = input("Enter Password: ")
    return password


main()
