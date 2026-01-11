# Write a program that manages a to-do list. 
# 
# Use a list of dictionaries, where each dictionary 
# represents a task with a 'description' (string) and 
# a 'completed' (boolean) key.
# Implement functions to
# - add a task
# - mark a task as complete
# - and view all tasks.



# 1. Initialize the list with some starting data
to_do_list = [
    {"description": "Buy groceries", "completed": False},
    {"description": "Finish Python script", "completed": True},
    {"description": "Go to the gym", "completed": False}
]

# 2. Function to add task to the list and mark as complete/incomplete
def add_task(new_task_dict):
  description_input = input("Type a task to do: ")
  completed_input = input("Is the task done? True or False? ")

  new_task_dict["description"] = description_input
  new_task_dict["completed"] = (completed_input.lower() == 'true') # Convert string to boolean


# 3. Ask user to create a task
new_task = {} # creates an empty dictionary
add_task(new_task) # Passes the empty dictionary to the function #2 

# print(new_task)

# 4. Add task to to do list
to_do_list.append(new_task)


# 5. View all tasks
print(to_do_list)