def transpose_matrix(matrix):
    # Check if matrix is empty
    if not matrix:
        return []

    # Dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the transpose
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    # Compute the transpose
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Get the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the original and transposed matrices
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)

'''
output:
Original Matrix:
[1, 2, 3]
[4, 5, 6]

Transposed Matrix:
[1, 4]
[2, 5]
[3, 6]

'''
