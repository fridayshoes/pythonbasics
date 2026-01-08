# Check for duplicates

# Objective: Detect duplicates using for-else.
# Outcome: Prints “Duplicate found: 3.”

numbers = [1, 3, 5, 3, 7]
seen = []
for n in numbers:
    if n in seen:
        print("Duplicate found:", n)
        break
    else:
        seen.append(n)
else:
    print("No duplicates found.")


# Duplicate found: 3