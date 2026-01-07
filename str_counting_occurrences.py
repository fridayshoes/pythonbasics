# Count occurrences of 'apple'

sentence = "apple banana apple orange"
words = sentence.split()
count = 0

for w in words:
  if w == "apple":
    count += 1
  else:
    print("Word 'apple occurs", count, "times.")


# Output

# Word 'apple occurs 1 times.
# Word 'apple occurs 2 times.