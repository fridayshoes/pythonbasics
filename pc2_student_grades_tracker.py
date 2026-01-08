# Example 1: Student grades tracker

# Objective: Store student names, scores, and 
# calculate the average; track unique names.
# Outcome: Prints average score and unique 
# student names.

# Track student grades

students = {"Alice": [85, 90], "Bob": [70, 75]}
unique_names = set(students.keys())
total = 0
count = 0
for scores in students.values():
    for s in scores:
        total += s
        count += 1
else:
    avg = total / count
    print("Average score:", avg)
    print("Unique students:", unique_names)

# Average score: 80.0
# Unique students: {'Alice', 'Bob'}