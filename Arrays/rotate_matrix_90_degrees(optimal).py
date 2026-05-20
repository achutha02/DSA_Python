matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)

# Transpose of matrix
for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Reverse each row of matrix
for i in range(n):
    for j in range(n // 2):
        matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]


print(matrix)


"""
Time Complexity: O(N^2) +O(N^2), to linearly iterate and find transpose of the matrix and another O(N2) to find the reverse of each row.

Space Complexity: O(1), as no extra space is being used.
"""