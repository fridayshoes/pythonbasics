# Find the largest number

# Objective: Find the largest number using for-else.
# Outcome: Prints “Largest number: 42.”


numbers = [10, 42, 5, 8]
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
else:
    print("Largest number:", max_num)

# Largest number: 42