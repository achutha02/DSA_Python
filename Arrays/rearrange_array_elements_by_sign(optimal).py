nums = [-4, 4, -4, 4, -4, 4]

m = 0
n = 1

ans = [0] * len(nums)


for i in range(len(nums)):
    if nums[i] > 0:
        ans[m] = nums[i]
        m += 2
        
    else:
        ans[n] = nums[i]
        n += 2

print(ans)



"""
Time Complexity: O(N), for traversing the array only once where N is the length of the array.

Space Complexity: O(N) to store the resultant array.
"""