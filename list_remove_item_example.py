# Remove all items from the list

# Objective: Remove items one by one using while-else.
# Outcome: Prints removed items and “All items removed.”

numbers = [1, 2, 3]
while numbers:
    removed = numbers.pop()
    print("Removed:", removed)
else:
    print("All items removed. List is empty:", numbers)

# Removed: 3
# Removed: 2
# Removed: 1
# All items removed. List is empty: []