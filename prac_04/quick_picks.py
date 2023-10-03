"""CP1404 Practical 04: Generates a number of quick picks based on a user input"""
import random

LOW_NUMBER = 1
HIGH_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick(NUMBERS_PER_QUICK_PICK)
        print_quick_pick(quick_pick)


def generate_quick_pick(numbers_per_quick_pick):
    quick_pick = []
    for j in range(numbers_per_quick_pick):
        number = random.randint(LOW_NUMBER, HIGH_NUMBER)
        while number in quick_pick:
            if number in quick_pick:
                number = random.randint(LOW_NUMBER, HIGH_NUMBER)
        quick_pick.append(number)
    return quick_pick


def print_quick_pick(quick_pick):
    max_length = len(str(HIGH_NUMBER))
    print(" ".join([f"{number:{max_length}}" for number in quick_pick]))


main()
