# Team Lab: Create a simple "shopping cart" checkout process. 
# 
# The cart is a list of prices. 
# 
# The program should loop through the cart, 
# - calculate the subtotal, 
# - apply a 10% discount if the subtotal is over $50, 
# - calculate tax, 
# - and print a final, formatted receipt. 
# 
# This requires loops and nested conditional logic.


cart = {
    "Milk (2L)": 1.45,
    "Eggs (12 pack)": 2.50,
    "Bread (Wholemeal)": 1.10,
    "Apples (6 pack)": 2.00,
    "Bananas (1kg)": 0.90,
    "Chicken Breast (500g)": 4.50,
    "Basmati Rice (1kg)": 1.80,
    "Pasta (500g)": 0.75,
    "Tomatoes (400g)": 1.20,
    "Cheddar Cheese (400g)": 3.40,
    "Toaster": 40.0
}

subtotal = 0.0
sub_discount = 0.0 
total = 0.0
tax = 0.20
tax_amount = 0
discount = 0.10
discount_amount = 0


for product, price in cart.items(): # interates the price (value) for each product (key) in the cart (dictionary items)
  subtotal = subtotal + price # adds each item to the sub_total
  print(f'{product:>30}', f' -  £{price:<1}') # prints each product and price as it iterates in a justified list
  if subtotal > 50: # checks to see if subtotal is greater than 50
    discount_amount = subtotal * discount # finds the value of the 10% discount from the subtoal
    sub_discount = subtotal - discount_amount # subtracts the discount amount from the subtotal
    tax_amount = sub_discount * tax # finds the value of the 20% tax amount from the subtotal
    total = sub_discount + tax_amount # add the tax amount to the subtotal to create the total


# Output justified below to produce a formatted receipt

print(f"{'Subtotal' :>30}", f' -  £{subtotal:<1}')
print(f"{'Discount 10%' :>30}", f' -  £{discount_amount:<1}')
print(f"{'Subtotal (inc. Discount 10%)' :>30}", f' -  £{sub_discount:<1}')
print(f"{'Tax 20%' :>30}", f' -  £{tax_amount:<1}')
print(f"{'Total' :>30}", f' -  £{total:<1}')



# Example of produced output below


#                     Milk (2L)  -  £1.45
#                Eggs (12 pack)  -  £2.5
#             Bread (Wholemeal)  -  £1.1
#               Apples (6 pack)  -  £2.0
#                 Bananas (1kg)  -  £0.9
#         Chicken Breast (500g)  -  £4.5
#            Basmati Rice (1kg)  -  £1.8
#                  Pasta (500g)  -  £0.75
#               Tomatoes (400g)  -  £1.2
#         Cheddar Cheese (400g)  -  £3.4
#                       Toaster  -  £40.0
#                      Subtotal  -  £59.6
#                  Discount 10%  -  £5.960000000000001
#  Subtotal (inc. Discount 10%)  -  £53.64
#                       Tax 20%  -  £10.728000000000002
#                         Total  -  £64.368





# print("Receipt:")




# UNFINISHED PROJECT