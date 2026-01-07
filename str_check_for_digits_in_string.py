# Check if a string contains digits

data = "abc123"

for ch in data:
  if ch.isdigit():
    print("Contains digits.")
    break
  else:
    print("No digitas found")

# Output

# No digitas found
# No digitas found
# No digitas found
# Contains digits.