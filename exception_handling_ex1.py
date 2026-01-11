# Write a script that asks the user for their age. 
# Use a ..except ValueError block to handle the 
# case where they enter non-numeric text. 
# Keep asking until they enter a valid age.


while True:
  try:
    age_input = int(input('Please enter your age: ')) # int used as code must an integer
    if age_input <= 0:
      raise ValueError("Age cannot be negative")
    if age_input >= 123:
      raise ValueError("Are you joking? Nobody has lived past 122 years!")
    else:
      print(f"Your age is {age_input}") # output if someone enter '4'
    break
  except ValueError as e:
        # This catches letters, symbols, or our custom negative age error
        print(f"Invalid input: {e}")
        print("Only numbers between 1 and 122 are acceptable")
  
  # except ValueError: # activates if someone enters 'four'
  #   print("Invalid input. Enter numeric value for your age") # prints this error
