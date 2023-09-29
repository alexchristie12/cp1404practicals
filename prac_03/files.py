"""CP1404 Practical 03"""
# Part 1
with open("name.txt", "w") as out_file:
    user_name = input("Enter your name: ")
    print(user_name, file=out_file)

# Part 2
with open("name.txt", "r") as in_file:
    user_name = in_file.readline().strip()
    print(f"Your name is: {user_name}")
