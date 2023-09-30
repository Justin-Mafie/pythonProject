from random import random  # Import the 'random' function from the 'random' module

# Generate a list of 20 random values between 0 and 1
l = [random() for i in range(20)]

# Generate a random value 'x'
x = random()

# Step 1: Sort the list in ascending order
sorted_l = sorted(l)

# Step 2: Find the index of the first element in the sorted list that is equal to or greater than x
index_of_first_greater_equal_x = next((i for i, value in enumerate(sorted_l) if value >= x), None)

# Print the original list, x, sorted list, and the index
print("Original list:", l)
print(f"Random value x: {x}")
print("Sorted list:", sorted_l)
print(f"Index of the first element >= x: {index_of_first_greater_equal_x}")
