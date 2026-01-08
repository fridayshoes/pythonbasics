# Example 10: Student progress report

# Objective: Combine all data types: 
# names (set), marks (list), averages (dict), progress range.
# Outcome: Prints report summary.

# Student progress report

names = {"Alice", "Bob"}
marks = [85, 90, 78, 92]
avg = sum(marks) / len(marks)
report = {"avg_score": avg, "total_students": len(names)}
progress = range(1, len(marks) + 1)
for p in progress:
    print("Progress step:", p)
else:
    print("Report:", report)

# Progress step: 1
# Progress step: 2
# Progress step: 3
# Progress step: 4
# Report: {'avg_score': 86.25, 'total_students': 2}