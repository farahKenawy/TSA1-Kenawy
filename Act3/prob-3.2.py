# Getting user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating first and last name
full_name = first_name + " " + last_name

# Displaying full name in upper and lower case
full_name_upper = full_name.upper()
full_name_lower = full_name.lower()

# Calculating the length of full name
full_name_length = len(full_name)

# Displaying results
print("\nFull Name:", full_name)
print("Full Name (Upper Case):", full_name_upper)
print("Full Name (Lower Case):", full_name_lower)
print("Length of Full Name:", full_name_length)
