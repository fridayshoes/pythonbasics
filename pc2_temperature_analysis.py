# Example 5: Temperature analysis

# Objective: Analyze temperature readings, find min, max, and average; store processed data in dict.
# Outcome: Prints temperature summary.

# Analyze temperature readings


temps = [22.5, 19.0, 25.5, 21.0]
summary = {"min": min(temps), "max": max(temps), "avg": sum(temps) / len(temps)}
if summary["avg"] > 20:
    print("Average temperature is comfortable.")
print("Summary:", summary)

# Average temperature is comfortable.
# Summary: {'min': 19.0, 'max': 25.5, 'avg': 22.0}