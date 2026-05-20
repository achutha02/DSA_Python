mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]
       ]

n = len(mat)

m = len(mat[0])

top = 0
left = 0

right = m-1
bottom = n-1

ans = []

while top <= bottom and left <= right:
    for i in range(left, right+1):
        ans.append(mat[top][i])
    top += 1

    for i in range(top, bottom+1):
        ans.append(mat[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left-1, -1):
            ans.append(mat[bottom][i])
        bottom -= 1
    
    if left <=right:
        for i in range(bottom, top-1, -1):
            ans.append(mat[i][left])
        left += 1

print(ans)




"""
Time Complexity:  O(MxN) since all the elements are being traversed once and there are total N x M elements ( M elements in each row and total N rows) so the time complexity will be O(N x M).

Space Complexity:  O(1) as extra space to store answer is not considered.
"""