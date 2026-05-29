nums = [-2, -3, 4, -1, -2, 1, 5, -3]

n = len(nums)

maxi = float('-inf')

curr_sum = 0

for i in range(n):
    curr_sum += nums[i]

    if curr_sum > maxi:
        maxi = curr_sum
    
    if curr_sum < 0:
        curr_sum = 0

print(maxi)




"""
Time Complexity:  O(N) for single traversal, here N is the size of the array.

Space Complexity: O(1), for not using any extra space.
"""

#This is also called Kadane's Algorithm