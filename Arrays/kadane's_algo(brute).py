nums = [2, 3, 5, -2, 7, -4]

n = len(nums)

max_sum = 0

for i in range(n):
    for j in range(i,n):
        curr_sum = 0

        for k in range(i, j+1):
            curr_sum += nums[k]

            if curr_sum > max_sum:
                max_sum = curr_sum

print(max_sum)




"""
Time Complexity: O(N^3), where N is the size of the array. Using three nested loops, each running approximately N times.

Space Complexity: O(1) no extra space used.
"""