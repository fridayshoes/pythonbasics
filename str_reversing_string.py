# Reverse a string using while loop

original = "python"
reversed_text = ""
i = len(original) -1
while i >= 0:
  reversed_text += original[i]
  i -= 1
else:
  print("Reversed string:", reversed_text)

# Output

# Reversed string: nohtyp