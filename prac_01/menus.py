user_name = str(input("Enter Name: "))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = str(input(">>> "))
while choice != "Q":
    if choice == "H":
        print(f"Hello {user_name}")
    elif choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid Input")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = str(input(">>> "))
print("Thank you!")
