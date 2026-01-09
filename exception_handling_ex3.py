# Write a script that tries to read a list of numbers from a 
# file named txt. 
# It should handle FileNotFoundError if the file 
# doesn't exist and ValueError if a line in the file 
# cannot be converted to a number.


numbers = []

try:
    with open("txt", "r") as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid number skipped: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'txt' was not found.")

else:
    print("Numbers read from file:", numbers)