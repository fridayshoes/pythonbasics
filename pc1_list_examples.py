# Example 1: Shopping Cart

# Process shopping cart with discounts

# Objective: Calculate shopping cart total with discounts
# Outcome: Prints receipt with 10% discount if total > $10


cart = [("Apple", 1.2, 3), ("Milk", 2.5, 1), ("Bread", 1.8, 2)]
total = 0.0
discount_threshold = 10

print("Receipt:")
for item in cart:
    name, price, quantity = item
    subtotal = price * quantity
    total += subtotal
    print(f"- {name} x{quantity}: ${subtotal:.2f}")

if total > discount_threshold:
    discount = total * 0.1
    total -= discount
    print(f"Discount applied: -${discount:.2f}")

print(f"Total due: ${total:.2f}")

# Receipt:
# - Apple x3: $3.60
# - Milk x1: $2.50
# - Bread x2: $3.60
# Total due: $9.70




 

# Example 2: Prime Number Finder

# Find prime numbers in a range

# Objective: Find primes using trial division
# Outcome: Lists primes ≤30: [2,3,5,7,11,13,17,19,23,29]

n = 30
primes = []
candidate = 2

while candidate <= n:
    is_prime = True
    for divisor in primes:
        if divisor * divisor > candidate:
            break
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)
    candidate += 1

print(f"Primes up to {n}:")
print(primes)


# Primes up to 30:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
