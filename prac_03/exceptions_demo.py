"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - You will get  a value error a non integer input is selected.
2. When will a ZeroDivisionError occur?
    - A zero division error will occur when the denominator is zero and the program attempts
        to divide by zero, the result of which is undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes, you would need to check if the denominator is valid (non-zero) before running the operation.
        This is the LBYL approach and I don't know why both approaches should be mixed
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be equal to zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")