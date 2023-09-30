import pandas as pd

# Create a dictionary with column names as keys and lists of column values as values
data = {
    'A': [3.1, 4.2, 1.5, 6.3],
    'B': [800, 150, 400, 210],
    'C': [1, 2, 2, 1]
}

# Create a DataFrame using the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
