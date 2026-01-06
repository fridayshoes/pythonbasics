# Count how many times 3 appears

numbers = [3, 1, 3, 7, 5]
count = 0

for num in numbers:
  if num == 3:
    count += 1
  else:
    print("3 appears", count, "times.")

# Output

# 3 appears 1 times.
# 3 appears 2 times.
# 3 appears 2 times.