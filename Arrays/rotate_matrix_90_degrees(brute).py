matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)

rotated = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated[j][n-1-i] = matrix[i][j]

for i in range(n):
    matrix[i] = rotated[i]

print(matrix)



"""
Time Complexity: O(N^2) +O(N^2), to linearly iterate and put elements into dummy matrix and another O(N2) to copy elements of dummy matrix back to original matrix.

Space Complexity: O(N^2), to store the elements in the dummy matrix.
"""
