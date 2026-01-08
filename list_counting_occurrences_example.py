# Count occurrences of 2

# Objective: Count how many times 2 appears.
# Outcome: Prints “2 appears 3 times.”

nums = [2, 3, 2, 4, 2]
count = 0
for n in nums:
    if n == 2:
        count += 1
else:
    print("2 appears", count, "times.")

# 2 appears 3 times.