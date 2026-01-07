# Write a script to validate a password. 
# The validation rules are: 
# 1. at least 8 characters, 
# 2. contains at least one uppercase letter, 
# 3. one lowercase letter, 
# 4. and one number. 
# 
# Use a for loop to iterate through the characters of the password string 
# and if statements with boolean flags to check if all conditions are met.

password = "123456A789c"

char_count = 0
uppercase_count = 0
lowercase_count = 0
digit_count = 0


for char in password:
  char_count +=1 # counts each character as it iterates through string
  if char.isupper():
    uppercase_count += 1 # counts uppercase chacrters
  elif char.islower():
    lowercase_count += 1 # counts lowercase characrters
  elif char.isdigit():
    digit_count += 1 # counts digits
  if char_count >= 8: 
    if uppercase_count >= 1:
      if lowercase_count >= 1:
        if digit_count >= 1:
          print("Password is GREAT!")
          break
else:
  print("Password fail")
   

# Debug

# print(char_count)
# print(uppercase_count)
# print(lowercase_count)
# print(digit_count)



# Output

# Password is GREAT!
