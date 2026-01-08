# Filter even numbers from a list

# Objective: Extract even numbers using for-else.
# Outcome: Prints “Even numbers: [2, 4, 6]”.

nums = [1, 2, 3, 4, 5, 6]
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
else:
    print("Even numbers:", evens)

# Even numbers: [2, 4, 6]