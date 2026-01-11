# Assignment

# Create a function get_int_from_user(prompt). This function should:

# Display the prompt to the user.
# Use a while loop and a ..except ValueError block to ensure 
# the user enters a valid integer.
# If the user enters anything else, it should print an error 
# message and ask again.
# Once a valid integer is entered, the function should return it.
# Write a small script to demonstrate your function works.



while True:
  try:
    # Displays prompt to user
    get_int_from_user = int(input("Type an integer please: "))
    # Returns the integer if it is valid
    print(f"Great! You typed: {get_int_from_user} as an integer")
    break
  except ValueError:
    print("Invalid input. Enter numbers only please") # prints this error


  