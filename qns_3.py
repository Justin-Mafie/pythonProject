def power(x, y):
    """
    This function takes two numbers, x and y, and returns x raised to the power of y.

    Args:
        x (float or int): The base number.
        y (float or int): The exponent.

    Returns:
        float or int: x raised to the power of y.
    """
    return x ** y

# List of pairs of numbers
number_pairs = [[5, 6], [5, 7], [4, 2], [3, 6], [9, 8], [1, 3], [9, 3], [7, 1], [5, 4], [2, 7], [9, 1], [9, 3], [2, 5]]

# Iterate through the list and call the 'power' function using argument unpacking
for pair in number_pairs:
    x, y = pair  # Unpack the pair into x and y
    result = power(x, y)  # Call the 'power' function with x and y
    print(f"{x}^{y} = {result}")  # Print the result of the power operation
