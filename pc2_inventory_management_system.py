# Example 2: Inventory management system
# Objective: Track inventory using a 
# dictionary; add items from a list; ensure 
# no duplicates using set.
# Outcome: Prints final inventory.

# Manage inventory

inventory = {}
items = ["apple", "banana", "apple", "orange"]
unique_items = set(items)
for item in unique_items:
    inventory[item] = inventory.get(item, 0) + 1
else:
    print("Final inventory:", inventory)

# Final inventory: {'banana': 1, 'apple': 1, 'orange': 1}