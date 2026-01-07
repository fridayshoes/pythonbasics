# Remove spaces from a string

text = " Hello World "
text_no_spaces = ""
i = 0

while i < len(text):
  if text[i] != " ":
    text_no_spaces += text[i]
  i += 1
else:
  print("String without spaces:", text_no_spaces)


# Output

# String without spaces: HelloWorld