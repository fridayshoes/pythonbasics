# Reverse a list manually

# Objective: Reverse a list manually.
# Outcome: Prints “Reversed list: [4, 3, 2, 1]”


original = [1, 2, 3, 4]
reversed_list = []
i = len(original) - 1
while i >= 0:
    reversed_list.append(original[i])
    i -= 1
else:
    print("Reversed list:", reversed_list)

# Reversed list: [4, 3, 2, 1]