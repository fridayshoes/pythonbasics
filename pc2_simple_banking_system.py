# Example 7: Simple banking system

# Objective: Track balances (float) by 
# account (dict); ensure valid accounts (set); calculate 
# total balance.
# Outcome: Prints all balances and total.

# Banking system


accounts = {"A123": 1500.0, "B456": 2500.0}
valid_accounts = set(accounts.keys())
total_balance = 0
for acc in valid_accounts:
    total_balance += accounts[acc]
else:
    print("Balances:", accounts)
    print("Total balance:", total_balance)


# Balances: {'A123': 1500.0, 'B456': 2500.0}
# Total balance: 4000.0
