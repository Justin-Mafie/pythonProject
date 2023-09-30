def seconds_to_time(seconds):
    """
    Convert the number of seconds past from a day to a time in hours, minutes, and seconds with AM or PM.

    Args:
        seconds (int): The number of seconds past from a day.

    Prints:
        str: A string representing the time in 'hh:mm:ss AM/PM' format or an error message if the hour is greater than 24.
    """
    # Calculate hours, minutes, and seconds
    hours = seconds // 3600  # Calculate the number of hours (3600 seconds in an hour)
    minutes = (seconds % 3600) // 60  # Calculate the number of minutes (60 seconds in a minute)
    seconds = seconds % 60  # Calculate the remaining seconds

    # Determine if it's AM or PM
    period = 'AM' if hours < 12 else 'PM'  # If hours are less than 12, it's AM; otherwise, it's PM

    # Adjust hours for AM/PM format
    if hours > 12:
        hours -= 12  # If hours are greater than 12, convert to 12-hour format

    # Handle the case when the hour is greater than 24
    if hours >= 24:
        print("Hour is greater than 24 hours in a day")  # Print an error message
    else:
        # Print the formatted time string
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d} {period}")

# Example usage:
seconds = 19667  # Example number of seconds elapsed from a day
seconds_to_time(seconds)
