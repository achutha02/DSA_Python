nums = [4, 5, 3, 7, 1, 2]

n = len(nums)

ans = float('-inf')

prefix = 1
suffix = 1

for i in range(n):
    if prefix == 0:
        prefix = 1
    if suffix == 0:
        suffix = 1
    
    prefix *= nums[i]
    suffix *= nums[n-i-1]

    ans = max(ans, max(prefix, suffix))

print(ans)



"""
Time Complexity: O(N), where N is the size of the array
Traversing the given array using single for loop takes linear time.

Space Complexity: O(1), as only couple of variables are used.
"""