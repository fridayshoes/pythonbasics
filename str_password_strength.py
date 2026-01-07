# Check password strength

password = "Python123"

if len(password) <6:
  print("Weak password")
elif password.isalnum() and any(ch.isdigit() for ch in password):
  print("Strong password")
else:
  print("Password needs numbers and letters")

# Output

# Strong password