# Adding items to a shopping list

# Adding items to a shopping list
# Objective: Use a list to store items and add until 
# limit is reached.
# Outcome: Prints items added and “Shopping list complete.”


shopping_list = []
items = ["milk", "bread", "eggs", "butter"]
i = 0
while i < len(items):
    shopping_list.append(items[i])
    print("Added:", items[i])
    i += 1
else:
    print("Shopping list complete:", shopping_list)


# Added: milk
# Added: bread
# Added: eggs
# Added: butter
# Shopping list complete: ['milk', 'bread', 'eggs', 'butter']