# Convert USD to EUR

rate = 0.92 # conversion rate

for usd in range(1,6):
  eur = usd * rate
  print(usd, "USD =", round(eur, 2), "EUR")
else:
  print("Conversion complete")

# Output

# 1 USD = 0.92 EUR
# 2 USD = 1.84 EUR
# 3 USD = 2.76 EUR
# 4 USD = 3.68 EUR
# 5 USD = 4.6 EUR
# Conversion complete