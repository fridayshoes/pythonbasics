# Example 1: RGB Color Mixer

# Mix RGB color tuples

# Objective: Blend two RGB colors
# Outcome: Creates purple (178, 0, 178) from 30% red + 70% blue


color1 = (255, 0, 0)   # Red
color2 = (0, 0, 255)   # Blue
ratio = 0.3
mixed = ()

for i in range(3):
    component = int(color1[i] * ratio + color2[i] * (1 - ratio))
    mixed += (component,)

print(f"Red: {color1}")
print(f"Blue: {color2}")
print(f"Mixed ({int(ratio*100)}% red): {mixed}")



# Red: (255, 0, 0)
# Blue: (0, 0, 255)
# Mixed (30% red): (76, 0, 178)



# Example 2: Coordinate Distance

# Calculate distance between points

# Objective: Calculate Euclidean distance
# Outcome: Computes distance ≈10.63 between (3,4) and (10,12)

pointA = (3, 4)
pointB = (10, 12)
squares = 0

for coord in zip(pointA, pointB):
    diff = coord[1] - coord[0]
    squares += diff ** 2

distance = squares ** 0.5
print(f"Distance between {pointA} and {pointB}: {distance:.2f} units")

# Distance between (3, 4) and (10, 12): 10.63 units