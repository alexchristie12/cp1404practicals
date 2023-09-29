"""CP1404 Practical 03"""
# Part 1
with open("name.txt", "w") as out_file:
    user_name = input("Enter your name: ")
    print(user_name, file=out_file)
print()

# Part 2
with open("name.txt", "r") as in_file:
    user_name = in_file.readline().strip()
    print(f"Your name is: {user_name}")
print()

# Part 3
with open("numbers.txt", "r") as in_file:
    total = 0
    for i in range(2):
        total += int(in_file.readline().strip())
    print(f"Total is: {total}")
print()

# Part 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line.strip())
    print(f"Total is: {total}")
