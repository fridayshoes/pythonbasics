# Write a script that asks the user for their age. 
# Use a ..except ValueError block to handle the 
# case where they enter non-numeric text. 
# Keep asking until they enter a valid age.


while True:
  try:
    age_input = int(input('Please enter your age')) # int used as code must an integer
    print(f"Your age is {age_input}") # output if someone enter '4'
    break
  except ValueError: # activates if someone enters 'four'
    print("Invalid input. Enter numeric value for your age") # prints this error
