# ATM withdrawel simulation
# Deduct money using while-else

balance = 50
withdraw = 10

while balance >= withdraw:
  print("Withdrawing", withdraw)
  balance -= withdraw
else:
  print("No more funds. Remaining balance:", balance)



# Output

# Withdrawing 10
# Withdrawing 10
# Withdrawing 10
# Withdrawing 10
# Withdrawing 10
# No more funds. Remaining balance: 0