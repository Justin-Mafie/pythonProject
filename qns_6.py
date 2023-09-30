def proportion_dict(numbers_list):
    """
    Calculate the proportion of list elements that are smaller than or equal to each element.

    Args:
        numbers_list (list of numbers): The list of numbers to process.

    Returns:
        dict: A dictionary where keys are numbers from the input list, and values are proportions.
    """
    result_dict = {}  # Initialize an empty dictionary to store the results

    # Count the occurrences of each number in the list
    count_dict = {}
    for num in numbers_list:
        count_dict[num] = count_dict.get(num, 0) + 1

    total_elements = len(numbers_list)  # Total number of elements in the list

    # Calculate the proportion for each unique number in the list
    for num in sorted(count_dict.keys()):
        count = count_dict[num]
        proportion = count / total_elements
        result_dict[num] = proportion

    return result_dict  # Return the resulting dictionary


# Example usage:
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5]
proportion_result = proportion_dict(numbers)
print(proportion_result)  # Print the resulting proportion dictionary
