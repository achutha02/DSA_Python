nums = [100, 4, 200, 1, 3, 2]

n = len(nums)

nums.sort()

longest = 1

cnt = 0

lastSmaller = float('-inf')

for i in range(n):
    if nums[i] - 1 == lastSmaller:
        cnt += 1
        lastSmaller = nums[i]
    
    elif nums[i] != lastSmaller:
        cnt = 1
        lastSmaller = nums[i]
    
    longest = max(longest, cnt)

print(longest)




"""
Time Complexity: O(NlogN) + O(N), here N is the size of the given array. Here, O(NlogN) is for sorting the array. To find the longest sequence, we use a loop that results in O(N).

Space Complexity:  O(1), as we are not using any extra space to solve this problem.
"""