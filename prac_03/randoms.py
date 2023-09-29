"""CP1404 Practical 3 randoms.py sections"""
import random

print(random.randint(5, 20))
# For line 3 the possible outputs are integers in the range of 5 to 20
print(random.randrange(3, 10, 2))
# For line 5 the smallest possible output is 3 and the highest is 10. It only prints odd numbers (as 3 is the start
# point). As it is only 1 increment from 3, 4 would not be a possible output
print(random.uniform(2.5, 5.5))
# For line 9 the smallest possible output is 2.6 and the highest is 5.5. It is a uniform random output.

# Random Number from 0-100 inclusive
print(random.uniform(0, 100))
