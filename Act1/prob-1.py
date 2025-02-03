# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the highest number
if num1 >= num2:
    if num1 >= num3:
        highest = num1
    else:
        highest = num3
elif num2 >= num3:
    highest = num2
else:
    highest = num3

print(f"The highest number is {highest}")

# Displaying numbers in descending order
if num1 >= num2:
    if num1 >= num3:
        if num2 >= num3:
            print(f"The numbers in descending order are: {num1}, {num2}, {num3}")
        else:
            print(f"The numbers in descending order are: {num1}, {num3}, {num2}")
    else:
        print(f"The numbers in descending order are: {num3}, {num1}, {num2}")
elif num2 >= num3:
    if num1 >= num3:
        print(f"The numbers in descending order are: {num2}, {num1}, {num3}")
    else:
        print(f"The numbers in descending order are: {num2}, {num3}, {num1}")
else:
    print(f"The numbers in descending order are: {num3}, {num2}, {num1}")
