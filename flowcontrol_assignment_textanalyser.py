# Create a script that analyzes a block of text (e.g., a multi-line string). The script must:

# 1. Iterate through each character of the text.
# 2. Count the number of uppercase letters, lowercase letters, digits, and spaces.
# 3. Use if-elif-else statements to categorize each character.
# 4. After the loop, print a report with the final counts for each category.


string = '''The quick brown fox
jumped over 200
lazy dogs''' # multi-line string uses ''' ''' triple quotes

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
upcase_count = 0
lowcase_count = 0
digit_count = 0
space_count = 0


for char in string:
  if char in uppercase_letters:
    upcase_count += 1
  elif char in lowercase_letters:
    lowcase_count +=1
  elif char.isdigit():
    digit_count += 1
  else:
    space_count += 1

print("The string has", upcase_count, "uppercase letters")
print("The string has", lowcase_count, "lowercase letters")
print("The string has", digit_count, "digits")
print("The string has", space_count, "spaces")


print("The string has", upcase_count, "uppercase letters,", lowcase_count, "lower case letters", digit_count, "digits and", space_count, "spaces.")


# Output

# The string has 1 uppercase letters
# The string has 33 lowercase letters
# The string has 3 digits
# The string has 8 spaces
# The string has 1 uppercase letters, 33 lower case letters 3 digits and 8 spaces.