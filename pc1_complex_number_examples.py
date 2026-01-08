# Example 1

# Identify quadrant of complex numbers

# Objective: Determine complex number quadrants
# Outcome: Classifies each number into coordinate quadrants

numbers = [3+4j, -2+3j, -1-1j, 2-3j]

for num in numbers:
    real = num.real
    imag = num.imag
    print(f"Number: {num}")
    
    if real > 0 and imag > 0:
        print("Quadrant I")
    elif real < 0 and imag > 0:
        print("Quadrant II")
    elif real < 0 and imag < 0:
        print("Quadrant III")
    else:
        print("Quadrant IV")

# Number: (3+4j)
# Quadrant I
# Number: (-2+3j)
# Quadrant II
# Number: (-1-1j)
# Quadrant III
# Number: (2-3j)
# Quadrant IV




# Example 2

# Find complex numbers with magnitude > 5

# Objective: Count complex numbers with magnitude >5
# Outcome: Identifies and counts qualifying numbers

values = [3+2j, 6+8j, 1+1j, 4+3j, 5+0j]
threshold = 5
count = 0

for val in values:
    magnitude = (val.real**2 + val.imag**2)**0.5
    if magnitude > threshold:
        count += 1
        print(f"{val} has magnitude {magnitude:.2f} (>5)")

print(f"{count} numbers exceed magnitude 5")



# (6+8j) has magnitude 10.00 (>5)
# 1 numbers exceed magnitude 5