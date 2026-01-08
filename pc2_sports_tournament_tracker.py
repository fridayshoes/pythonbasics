# Example 8: Sports tournament tracker

# Objective: Track teams and scores; store 
# results as tuples; update wins in dictionary.
# Outcome: Prints final scores dictionary.

# Tournament tracker

matches = [("TeamA", "TeamB", 2, 1), ("TeamC", "TeamA", 0, 3)]
scores = {}
for match in matches:
    winner = match[0] if match[2] > match[3] else match[1]
    scores[winner] = scores.get(winner, 0) + 1
else:
    print("Final scores:", scores)

# Final scores: {'TeamA': 2}