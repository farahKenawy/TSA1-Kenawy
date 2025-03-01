# 1. How does the format() function help in combining variables with text in Python?
#    The format() function allows you to insert variables into a string in a structured way.

# Example using format()
name = "Alice"
age = 25
message = "Hello, my name is {} and I am {} years old.".format(name, age)
print(message)

# Example using f-string (recommended)
message = f"Hello, my name is {name} and I am {age} years old."
print(message)


# 2. Difference Between 'r' (Read Mode) and 'w' (Write Mode) in File Handling
#    - 'r' (Read Mode): Opens a file for reading. If the file does not exist, an error occurs.
#    - 'w' (Write Mode): Opens a file for writing. If the file exists, it overwrites its content.
#    - Use 'r' when you want to read a file without modifying it.
#    - Use 'w' when you want to create or overwrite a file.

# Read mode ('r') - Reading a file
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")

# Write mode ('w') - Overwriting a file
with open("example.txt", "w") as file:
    file.write("This is new content!")


# 3. What is String Slicing in Python?
#    String slicing allows you to extract a part (substring) from a larger string using indexing.

text = "Hello, World!"
substring = text[0:5]  # Extracts characters from index 0 to 4 (not including 5)
print(substring)  # Output: Hello

# Using negative indexing
print(text[-6:])  # Extracts last 6 characters (Output: World!)


# 4. Purpose of Using 'a' (Append Mode) Instead of 'w' Mode
#    - 'a' (Append Mode) adds new content to a file without removing existing data.
#    - 'w' (Write Mode) overwrites the file, deleting previous content.

# Append mode ('a') - Adds new content without erasing existing data
with open("log.txt", "a") as file:
    file.write("New log entry added!\n")


# 5. Python Code to Open and Read a File (Handling Missing File)
#    - This ensures the program does not crash if the file is missing.

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist.")
