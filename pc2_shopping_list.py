# Objective: Use a tuple for items, dictionary for 
# prices, and calculate total using range.
# Outcome: Prints total price and purchased items.

# Shopping list and prices


items = ("milk", "bread", "eggs")
prices = {"milk": 1.5, "bread": 2.0, "eggs": 3.0}
total = 0.0
for i in range(len(items)):
    total += prices[items[i]]
else:
    print("Purchased items:", items)
    print("Total price:", total)


# Purchased items: ('milk', 'bread', 'eggs')
# Total price: 6.5