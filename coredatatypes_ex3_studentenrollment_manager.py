# You are given two lists of student IDs, one for students 
# enrolled in Math and one for students in Science. 
# 
# Write a script that uses sets to find: 
# (a) Students enrolled in both courses. 
# (b) All unique students enrolled in either course. 
# (c) Students enrolled in Math but not Science.


# Lists of student IDs
math_students = [101, 102, 103, 104, 105]
science_students = [103, 104, 106, 107, 108]


# 1 Convert lists to sets
maths_student_set = set(math_students)
science_students_set = set(science_students)

# print(maths_student_set)
# print(science_student_set)

# 2 Find students enrolled in both courses and only one course

both_courses_students = maths_student_set & science_students_set # uses & intersection operator ti find common elements
unique_courses_students = maths_student_set ^ science_students_set # ^ symetric difference operator to find the uncommon elements 
print(f"Student IDs enrolled in both courses {both_courses_students}")
print(f"Student IDs enrolled in only one course {unique_courses_students}")

# Find students enrolled in maths but not science

maths_not_science_students = maths_student_set - science_students_set
if maths_not_science_students: # if this is True it will print the student IDs
  print(f"Students enrolled in maths, but not science are: {maths_not_science_students}")
else: # if there are no maths students not in science it will print no difference found
  print("No difference found")