nums = [4, 5, 3, 7, 1, 2]

n = len(nums)

result = nums[0]

for i in range(n):
    p = nums[i]
    for j in range(i+1, n):
        result = max(result, p)

        p *= nums[j]
    
    result = max(result, p)

print(result)


"""
Time Complexity: O(N^2) for using 2 nested loops for finding all possible subarrays and their product. Here N is the size of the array.

Space Complexity: O(1) as no additional space is used apart from the input array.
"""
