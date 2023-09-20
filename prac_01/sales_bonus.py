"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

total_sales = float(input("Enter Your Sales: $"))
if total_sales < 1000:
    bonus_rate = 0.1
else:
    bonus_rate = 0.15

bonus_amount = total_sales * bonus_rate
print(f"Your Bonus is: ${bonus_amount}")
