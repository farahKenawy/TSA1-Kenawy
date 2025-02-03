# Taking input from the user
number = int(input("Enter a number to check if it is prime: "))

# Check if the number is less than or equal to 1
if number <= 1:
    print(f"{number} is not a prime number.")
else:
    # Loop to check divisibility from 2 up to the square root of the number
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
