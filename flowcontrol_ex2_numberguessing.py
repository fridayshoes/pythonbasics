# Create a number guessing game. 

# The program should pick a random number between 1 and 100 and the user has to guess it. 
# The program should provide "Too high" or "Too low" hints.
# Use a while loop that terminates when the user guesses correctly.




import random # imports the random module

number = random.randint(1, 100) # uses the random module to create a random number from a range

print (number) # prints the randomly generated number so we can see to test game

guess =()

while number != guess:
  guess = int(input("Guess number between 1 and 100")) # waits for user to input an integer
  if guess > number:
    print ("Too High")
  if guess < number:
    print ("Too Low")

print ("You guessed the number!") # exits the while loop when number == guess





