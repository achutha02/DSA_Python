nums = [2, 3, 5, -2, 7, -4]

n = len(nums)

max_sum = 0

for i in range(n):
    curr_sum = 0
    for j in range(i, n):
        curr_sum += nums[j]
        if curr_sum > max_sum:
            max_sum = curr_sum

print(max_sum)




"""
Time Complexity: O(N^2), for using two nested loops, each running approximately N times, here N is the size of the array.

Space Complexity: O(1) for not using any extra space.
"""