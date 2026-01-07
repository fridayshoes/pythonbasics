# Find the longest word in a sentence

text = "cat dog elephant ant"
longest = ""

for w in text.split():
  if len(w) > len(longest):
    longest = w
  else:
    print("Longest word:", longest)


# Output

# Longest word: cat
# Longest word: elephant