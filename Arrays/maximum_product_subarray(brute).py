nums = [4, 5, 3, 7, 1, 2]

n = len(nums)

result = float('-inf')

for i in range(n):
    for j in range(i, n):
        prod = 1
        for k in range(i, j+1):
            prod *= nums[k]

        if prod > result:
            result = prod

print(result)


"""
Time Complexity: O(N^3) for using 3 nested loops for finding all possible subarrays and their product. Here N is the size of the array.

Space Complexity: (1), as no additional space is used apart from the input array.
"""