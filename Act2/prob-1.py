# Taking input from the user for first and last terms
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

# Calculating the sum of numbers from first term to last term
sum_of_numbers = sum(range(first_term, last_term + 1))

# Displaying the result
print(f"The sum of the numbers from {first_term} to {last_term} is {sum_of_numbers}")
