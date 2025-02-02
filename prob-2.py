def sum_of_digits(input_string):
    sum = 0
    for char in input_string:
        if char.isdigit():
            sum += int(char)
    print(f"Sum of Digits: {sum}")

while True:
    user_input = input("Enter a string (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    sum_of_digits(user_input)