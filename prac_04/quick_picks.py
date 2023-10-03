"""CP1404 Practical 04: Generates a number of quick picks based on a user input"""
import random

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(6):
        number = random.randint(1, 45)
        while number in quick_pick:
            if number in quick_pick:
                number = random.randint(1, 45)
        quick_pick.append(number)
    print(" ".join([f"{number:2}" for number in quick_pick]))
