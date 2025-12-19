# Write a script that iterates through a list of dictionaries (e.g., student records)
# Uses a for loop and an if statement to find and print the name of the student with the highest score.


student_record = {
  "Sarah": 20,
  "James": 35,
  "Beth": 61,
  "David": 98,
  "Anna": 15
}

max_score = 0
top_student = ()

for student, score in student_record.items(): # interates score (value) for each student (key) in the student record (dictionary items)
  if score > max_score: # looks to see if the score is higher than the max_score
    print(student) # for debug purposes
    max_score = score # updates max_score
    top_student = student # updates the top_student

print(top_student) # prints the name of the top_student when all scores have been compared 
