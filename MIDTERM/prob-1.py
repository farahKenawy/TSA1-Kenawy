def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for index, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {index}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains invalid data.")

# Run the function with the filename 'numbers.txt, take the path of the file'
process_file(r"C:\Users\liltiger_30\OneDrive\Documents\2425SY-2T\Python\TSA1-Kenawy\Midterm\numbers.txt")
