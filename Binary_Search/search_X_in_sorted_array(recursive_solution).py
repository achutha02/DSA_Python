def func(nums, low, high, target):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid
    
    elif nums[mid] > target:
        return func(nums, low, mid - 1, target)
    
    else:
        return func(nums, mid + 1, high, target)

nums = [-1, 0, 3, 5, 9, 12]

n = len(nums)

ind = func(nums, 0, n-1, 9)

print(ind)




"""
Time Complexity: O(logN), where N is the size of the array
In each step, the search space is divided into two halves. In the worst case, this process will continue until the search space can no longer be divided and the number of divisions required to reduce the array size to one is log(N), making the overall time complexity O(logN).

Space Complexity: O(logN), due to the recursion stack space.
"""