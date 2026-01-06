#Guess the secret number

secret = 7
guess = 0

while guess !=secret:
  guess += 1 # trying numbers 1,2,3....
  print("Guessing:", guess)
else:
  print("Correct! The secret number is", secret)

# Output

# Guessing: 1
# Guessing: 2
# Guessing: 3
# Guessing: 4
# Guessing: 5
# Guessing: 6
# Guessing: 7
# Correct! The secret number is 7