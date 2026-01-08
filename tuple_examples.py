# Example 1: Accessing elements of a tuple

# Objective: Print each item in a tuple using for-else.
# Outcome: Prints all fruits and “All items printed.”
 

# Access each item in a tuple

fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print("Fruit:", fruit)
else:
    print("All items printed.")

# Fruit: apple
# Fruit: banana
# Fruit: cherry
# All items printed.




# Example 2: Checking if an item exists

# Objective: Search for an item using if-else.
# Outcome: Prints “Banana is in the tuple.”

# Check for an item in the tuple

fruits = ("apple", "banana", "cherry")
if "banana" in fruits:
    print("Banana is in the tuple.")
else:
    print("Banana not found.")

# Banana is in the tuple.





# Example 3: Tuple immutability

# Objective: Demonstrate that tuples cannot be changed.
# Outcome: Prints “Tuples are immutable.”

# Attempt to modify a tuple

colors = ("red", "blue", "green")
try_index = 1
if try_index < len(colors):
    print("Tuples are immutable. Cannot change:", colors[try_index])
else:
    print("Index out of range.")

# Tuples are immutable. Cannot change: blue





# Example 4: Nested tuple access

# Objective: Access elements inside nested tuples.
# Outcome: Prints “Nested element: 3.”

# Access elements in nested tuple

nested = (1, 2, (3, 4))
if isinstance(nested[2], tuple):
    print("Nested element:", nested[2][0])
else:
    print("No nested tuple found.")


# Nested element: 3  

 

# Example 5: Using tuple in a while loop

# Objective: Print items using while-else.
# Outcome: Prints all colors and “Finished printing colors.”

# Print tuple items using while loop

colors = ("red", "blue", "green")
i = 0
while i < len(colors):
    print("Color:", colors[i])
    i += 1
else:
    print("Finished printing colors.")

# Color: red
# Color: blue
# Color: green
# Finished printing colors.





# Example 6: Counting elements in a tuple

# Objective: Count occurrences of “apple.”
# Outcome: Prints “Apple occurs 2 times.”

# Count how many times 'apple' occurs

fruits = ("apple", "banana", "apple", "cherry")
count = 0
for fruit in fruits:
    if fruit == "apple":
        count += 1
else:
    print("Apple occurs", count, "times.")

# Apple occurs 2 times.


 

# Example 7: Comparing two tuples

# Objective: Check if tuples have the same elements.
# Outcome: Prints “Tuples match.”

# Compare two tuples

t1 = (1, 2, 3)
t2 = (1, 2, 3)
if t1 == t2:
    print("Tuples match.")
else:
    print("Tuples do not match.")

# Tuples match.


 

# Example 8: Finding the largest number in a tuple

# Objective: Identify the largest number using for-else.
# Outcome: Prints “Largest number: 9.”

# Find the largest number

nums = (3, 5, 9, 2)
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
else:
    print("Largest number:", largest)


# Largest number: 9




# Example 9: Checking for empty tuple

# Objective: Check if tuple is empty.
# Outcome: Prints “Tuple is empty.”

# Check for empty tuple

t = ()
if len(t) == 0:
    print("Tuple is empty.")
else:
    print("Tuple has elements.")


# Tuple is empty.

 

# Example 10: Tuple unpacking

# Objective: Assign tuple values to variables.
# Outcome: Prints “Name: John, Age: 25, City: London.”

# Unpack tuple values

person = ("John", 25, "London")
if len(person) == 3:
    name, age, city = person
    print("Name:", name, "Age:", age, "City:", city)
else:
    print("Tuple does not have exactly 3 elements.")

# Name: John Age: 25 City: London