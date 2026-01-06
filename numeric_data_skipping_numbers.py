# Print numbers, skipping those divisible by 3

for i in range(1, 11):
  if i % 3 == 0:
    continue
  print(i)
else:
  print("Skipped numbers divisible by 3.")

# Output

# 1
# 2
# 4
# 5
# 7
# 8
# 10
# Skipped numbers divisible by 3.