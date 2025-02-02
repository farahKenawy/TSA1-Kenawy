def pattern_a():
    rows = 5
    print("Pattern A:\n")
    for i in range(1, rows + 1):
        for j in range(rows - i): # Print leading spaces
            print(" ", end="")
        for k in range(1, i + 1): # Print increasing numbers
            print(k, end="")
        print()  # Newline

def pattern_b():
    row = 1
    print("Pattern B:\n")
    sequence = [1, 3, 5, 6, 7]  # The sequence of numbers for each row
    while row <= 5:
        num = sequence[row - 1] # Get the current number from the sequence
        count = 0 # Print number from the sequence in required reps
        while count < num:
            print(num, end="")
            count += 1

        spaces = 5 - row # Print leading spaces
        while spaces > 0:
            print(" ", end="")
            spaces -= 1
        
        print()  # Newline after each row
        row += 1

# Display both patterns
pattern_a()
print()  # Add space between patterns
pattern_b()