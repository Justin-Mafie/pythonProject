import math  # Import the 'math' library for mathematical functions

def area_percentage_coverage(radius1, radius2):
    """
    Calculate the percentage of the area of the larger circle covered by the smaller circle.

    Args:
        radius1 (int): The radius of the first circle.
        radius2 (int): The radius of the second circle.

    Returns:
        float: The percentage of the area of the larger circle covered by the smaller circle.
    """
    # Calculate the area of circles
    area1 = math.pi * (radius1 ** 2)  # Area of the first circle
    area2 = math.pi * (radius2 ** 2)  # Area of the second circle

    # Determine which circle is larger
    larger_radius = max(radius1, radius2)
    smaller_radius = min(radius1, radius2)

    # Calculate the percentage of the area of the larger circle covered by the smaller circle
    coverage_percentage = (area2 / area1) * 100 if area1 != 0 else 0

    return coverage_percentage

# Example usage:
radius1 = 5
radius2 = 3

percentage_coverage = area_percentage_coverage(radius1, radius2)
print(f"The percentage of the area covered by the smaller circle: {percentage_coverage}%")
