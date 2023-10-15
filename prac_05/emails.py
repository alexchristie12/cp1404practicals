"""
CP1404 Practical 05: Emails
Estimated Time: 20 minutes
Actual Time: 26 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        yes_no_input = input(f"Is your name {name}? (Y/n): ")
        if yes_no_input == 'Y' or yes_no_input == '':
            email_to_name[email] = name
        else:
            email_to_name[email] = input("Name: ")
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    email_name = email.split('@')[0]
    return " ".join([name.title() for name in email_name.split(".")])


if __name__ == "__main__":
    main()
