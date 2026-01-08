# Example 9: Data encoding and decoding

# Objective: Encode string data into bytes; decode 
# back; verify equality.
# Outcome: Prints encoded bytes and decoded string.

# Encode and decode string data


text = "Hello Python"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
if decoded == text:
    print("Encoding and decoding successful.")
    print("Encoded:", encoded)
else:
    print("Mismatch in decoding.")


# Encoding and decoding successful.
# Encoded: b'Hello Python'