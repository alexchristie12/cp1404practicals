"""CP1404 Practical 04 Lists Warmup"""
# Part 0
numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0]           => 3
# numbers[-1]          => 2
# numbers[3]           => 1
# numbers[:-1]         => [3, 1, 4, 1, 5, 9]
# numbers[3:4]         => [1]
# 5 in numbers         => True
# 7 in numbers         => False
# "3" in numbers       => False
# numbers + [6, 5, 3]  => [3, 1, 4, 1, 5, 9, 2, 6, 5, 3

# Part 1
numbers[0] = "ten"
print(numbers)
# Part 2
numbers[-1] = 1
print(numbers)
# Part 3
print(numbers[2:])
# Part 4
print(9 in numbers)
