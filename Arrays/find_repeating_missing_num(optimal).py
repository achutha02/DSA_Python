nums = [3, 1, 2, 5, 4, 6, 7, 5]

n = len(nums)

SN = (n * (n+1)) // 2

S2N = (n * (n+1) * (2*n+1)) // 6

S = 0
S2 = 0

for num in nums:
    S += num
    S2 += num * num

val1 = S - SN

val2 = S2 - S2N

val2 = val2 // val1

x = (val1 + val2) // 2

y = val2 - x

print([x,y])






"""
Time Complexity: O(N), as a single loop is used, where N is the size of the given array.

Space Complexity: O(1) no extra space is used.

"""
