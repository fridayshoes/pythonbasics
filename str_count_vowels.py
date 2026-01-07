# Count vowels in a string

text = "hello world"
vowels = "aeiou"
count = 0

for char in text:
  if char in vowels:
    count += 1
  else:
    print("Number of vowels:", count)


# Output

# Number of vowels: 0
# Number of vowels: 1
# Number of vowels: 1
# Number of vowels: 2
# Number of vowels: 2
# Number of vowels: 3
# Number of vowels: 3
# Number of vowels: 3