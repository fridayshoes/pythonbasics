# Individual Lab: Create a "Contact Book" program. 
# 
# The main data structure should be a dictionary where keys 
# are contact names and values are another dictionary containing 
# their phone number and email. 
# 
# The program should allow the user to add, look up, and delete contacts.


# A 'nested' dictionary of contacts
contacts = {
    "Alice Smith": {
        "phone": "555-0101",
        "email": "alice@example.com"
    },
    "Bob Jones": {
        "phone": "555-0202",
        "email": "bob@example.com"
    },
    "Charlie Brown": {
        "phone": "555-0303",
        "email": "charlie@example.com"
    }
}

# print(contacts)

# 1. Function to make a 'nested' dictionary contact
new_contact = {}

def add_contact(directory, name, phone, email):
  directory[name] = {
        "phone": phone,
        "email": email
    }


# 2 Call for user input 
name = input("Add contact name: ")
phone = input("Add contact phone number: ")
email = input("Add contact email address: ")

# Call function in #1 to create the contact using above data
add_contact(new_contact, name, phone, email)


# print(new_contact)

# 3 Add function to merge new_contact dictionary into contacts dictionary
for key in new_contact:
  contacts[key] = new_contact[key]
  print(contacts)

# 4 Look up a contact
def lookup_contact(directory, name):
    # .get() is safer than square brackets because it won't crash 
    # if the name doesn't exist.
    contact_info = directory.get(name) # gets the contacts info using the name
    
    # print(contact_info)

    if contact_info:
        print(f"\n--- Found: {name} ---")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email']}")
        return contact_info
    else:
        print(f"\nError: '{name}' not found in directory.")
        return None

# Ask user to input name they want to lookup
name = input(("Type contact name to lookup: ")) # Must be exact name and case

# Call the function in #4
lookup_contact(contacts, name)


# 5 Delete a contact

def delete_contact(directory, name):
    
    contact_info = directory.get(name) # gets the contacts info using the name

    # print(contact_info)

    if contact_info: # if contact info exists, will delete it 
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found.")


# Ask user to input name they want to delete
name = input(("Type contact name to delete: "))

# Call the function in #5
delete_contact(contacts, name)



# 6 Print the final contacts dictionary to see all changes
print(contacts)
       
    



# name = input(("Type a contact name to delete: "))
# delete_contact(contacts, name)

