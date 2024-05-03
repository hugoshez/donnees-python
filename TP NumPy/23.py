import numpy as np

# Define the 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate the inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

# Print the inverse matrix
print(inverse_matrix)