# Example 1

# Check if temperatures are below freezing
temperatures = [4, -2, 5, -5, 0, 3, -1, -3]
negative_count = 0

for temp in temperatures:
    if temp < 0:
        print(f"{temp}°C: Freezing!")
        negative_count += 1
    elif temp == 0:
        print("0°C: Ice point!")
    else:
        print(f"{temp}°C: Above freezing")

print(f"Total freezing days: {negative_count}")


# 4°C: Above freezing
# -2°C: Freezing!
# 5°C: Above freezing
# -5°C: Freezing!
# 0°C: Ice point!
# 3°C: Above freezing
# -1°C: Freezing!
# -3°C: Freezing!
# Total freezing days: 4


# Example 2

# Generate multiplication table for a number
number = 7
counter = 1

while counter <= 10:
    result = number * counter
    print(f"{number} x {counter} = {result}")
    counter += 1
else:
    print("Multiplication table complete!")

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
# Multiplication table complete!