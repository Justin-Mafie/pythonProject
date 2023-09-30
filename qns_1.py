import math  # Import the math library for factorial calculations

# Using a loop to calculate the factorial
result = 1  # Initialize the result to 1
i = 1       # Initialize the starting number to 1

# Continue looping until the result is equal to or greater than 10^8
while result < 10**8:
    i += 1            # Increment the current number by 1
    result *= i       # Multiply the result by the current number

# Print the smallest value of 'i' such that the result is >= 10^8
print(f"Using a loop: The smallest value of 'i' such that i! (factorial) is greater than or equal to 10^8 is: {i}")
print(f"{i}! = {result}")

# Using the math library to calculate the factorial
result = 1  # Reset the result to 1
i = 1       # Reset the starting number to 1

# Continue looping until the result is equal to or greater than 10^8
while result < 10**8:
    i += 1            # Increment the current number by 1
    result = math.factorial(i)  # Calculate the factorial using the math library

# Print the smallest value of 'i' such that the result is >= 10^8
print(f"Using the math library: The smallest value of 'i' such that i! (factorial) is greater than or equal to 10^8 is: {i}")
print(f"{i}! = {result}")
