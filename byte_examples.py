# Bytes (bytes)

# Example 1: Creating bytes from a string
# Objective: Convert a string to bytes using UTF-8 encoding.
# Outcome: Prints b'hello'.

# Convert string to bytes

text = "hello"
byte_data = text.encode("utf-8")
if isinstance(byte_data, bytes):
    print(byte_data)
else:
    print("Conversion failed.")

# b'hello'





# Example 2: Checking if a byte sequence contains a value
# Objective: Use if-else to search for a byte value.
# Outcome: Prints “Byte found.”

# Check if byte value exists

data = b"python"
if 112 in data:  # ASCII for 'p'
    print("Byte found.")
else:
    print("Byte not found.")

# Byte found.




# Example 3: Iterating over bytes

# Objective: Print each byte value using for-else.
# Outcome: Prints ASCII values of “ABC” and “Iteration complete.”

# Iterate over bytes

b = b"ABC"
for byte in b:
    print(byte)
else:
    print("Iteration complete.")

# 65
# 66
# 67
# Iteration complete. 




# Example 4: Counting specific byte occurrences

# Objective: Count how many times byte 97 ('a') appears.
# Outcome: Prints “Byte 'a' occurs 3 times.”

# Count specific byte

b = b"banana"
count = 0
for byte in b:
    if byte == 97:
        count += 1
else:
    print("Byte 'a' occurs", count, "times.")

# Byte 'a' occurs 3 times.



# Example 5: Converting bytes back to string

# Objective: Decode bytes to string.
# Outcome: Prints “Decoded string: hello”.

# Convert bytes back to string

b = b"hello"
decoded = b.decode("utf-8")
if decoded == "hello":
    print("Decoded string:", decoded)
else:
    print("Decoding failed.")

# Decoded string: hello




# Example 6: Slicing bytes

# Objective: Demonstrate slicing a byte object.
# Outcome: Prints b'Py'.

# Slice bytes

b = b"Python"
part = b[:2]
if part == b"Py":
    print(part)
else:
    print("Slice mismatch.")

# b'Py'



# Example 7: Creating bytes from integers

# Objective: Build bytes from integer values.
# Outcome: Prints b'ABC'.

# Create bytes from integers

byte_array = bytes([65, 66, 67])  # ASCII codes
if byte_array == b"ABC":
    print(byte_array)
else:
    print("Bytes creation failed.")

# b'ABC'



# Example 8: Comparing two byte sequences

# Objective: Compare equality of two byte objects.
# Outcome: Prints “Byte sequences are equal.”

# Compare two bytes

b1 = b"data"
b2 = b"data"
if b1 == b2:
    print("Byte sequences are equal.")
else:
    print("Byte sequences are different.")

# Byte sequences are equal.



# Example 9: Removing spaces from byte data

# Objective: Remove space bytes using while-else.
# Outcome: Prints b'HelloWorld'.

# Remove spaces from bytes

data = b" Hello World "
result = b""
i = 0
while i < len(data):
    if data[i] != 32:  # ASCII for space
        result += bytes([data[i]])
    i += 1
else:
    print(result)

# b'HelloWorld'




# Example 10: Checking if bytes are empty

# Objective: Verify if a byte object is empty using if-else.
# Outcome: Prints “Byte object is empty.”

# Check for empty bytes

b = b""
if len(b) == 0:
    print("Byte object is empty.")
else:
    print("Byte object has data.")

# Byte object is empty.