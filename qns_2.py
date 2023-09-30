def string_lengths_to_dict(string_list):
    """
    This function takes a list of strings as input and returns a dictionary
    where the keys are the strings and the values are the lengths of the strings.

    Args:
        string_list (list of str): The list of strings to process.

    Returns:
        dict: A dictionary where keys are strings and values are their lengths.
    """
    result_dict = {}  # Initialize an empty dictionary to store the results

    # Iterate through the list of strings
    for string in string_list:
        # Use the string as the key and its length as the value in the dictionary
        result_dict[string] = len(string)

    return result_dict  # Return the resulting dictionary


# Example usage:
input_strings = ["apple", "banana", "cherry", "date"]
length_dict = string_lengths_to_dict(input_strings)
print(length_dict)  # Print the resulting dictionary
