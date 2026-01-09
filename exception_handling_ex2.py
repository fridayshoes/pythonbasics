# Create a function that takes two numbers and returns their 
# division. 
# The function should use a ..except ZeroDivisionError block 
# to return None if the second number is zero.


def numberdivider(a,b):
  try:
    return a / b
  except ZeroDivisionError:
    return None

print(numberdivider(10, 2)) # Will return 5.0
print(numberdivider(12, 5)) # Will return 2.4
print(numberdivider(14, 0)) # Will return None