"""Printing the entire row of given row number"""

r = 5

ans = [0] * r

ans[0] = 1

for i in range(1, r):
    ans[i] = (ans[i-1] * (r - i)) // i

print(ans)



"""
Time Complexity: O(R), where R is the given row number.
A simple loop is used that runs R times and performs constant time oprations in each iteration resulting in a linear time complexity.

Space Complexity: O(1), as no extra space is used.
"""