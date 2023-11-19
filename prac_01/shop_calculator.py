"""
shop_calculator.py: This script calculates the total cost of a number of items
"""

DISCOUNT_RATE = 0.1
total_cost = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid Input!")
    number_of_items = int(input("Number of Items: "))

for item_number in range(number_of_items):
    item_price = float(input(f"Price of item {item_number + 1}: "))
    total_cost += item_price

if total_cost > 100:
    total_cost = total_cost - total_cost * DISCOUNT_RATE

print(f"The total cost of {number_of_items} items is ${total_cost:.2f}")
