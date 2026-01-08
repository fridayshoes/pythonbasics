# Example 1: Stepped Countdown

# Count down with custom steps

# Objective: Count down from 20 to 0 in -3 steps
# Outcome: Prints 20,17,14,11,8,5,2 then "Ignition!"


start = 20
end = 0
step = -3
current = start

print("Countdown:")
while current > end:
    print(current)
    current += step
else:
    print("Ignition!")

# Countdown:
# 20
# 17
# 14
# 11
# 8
# 5
# 2
# Ignition!

 

# Example 2: Grid Generator

# Generate grid coordinates

# Objective: Create coordinate pairs for grid
# Outcome: [(1,1),(1,2),(2,1),(2,2),(3,1),(3,2)]

rows = range(1, 4)
cols = range(1, 3)
grid = []

for r in rows:
    for c in cols:
        grid.append((r, c))

print("2x3 Grid Coordinates:")
print(grid)


# 2x3 Grid Coordinates:
# [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
