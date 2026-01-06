# Find the largest number in a list

numbers = [5, 9, 2, 10, 3] # lists use [] brackets
largest = numbers[0]

for num in numbers:
  if num > largest:
    largest = num
  else:
    print("The largest number is:", largest)

# Output

# The largest number is: 5
# The largest number is: 9
# The largest number is: 10