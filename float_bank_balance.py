# Deducts amounts until balance is too low

balance = 100.0
withdrawel = 15.5

while balance > 20.0:
  print("Balance before withdrawel:", balance)
  balance -= withdrawel
else:
  print("Low balance warning. Final balance:", balance)


# Output

# alance before withdrawel: 100.0
# Balance before withdrawel: 84.5
# Balance before withdrawel: 69.0
# Balance before withdrawel: 53.5
# Balance before withdrawel: 38.0
# Balance before withdrawel: 22.5
# Low balance warning. Final balance: 7.0