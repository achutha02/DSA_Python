nums = [-1, 0, 3, 5, 9, 12]

target = 9

n = len(nums)

low = 0
high = n-1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print(mid)
        break
    
    elif target > nums[mid]:
        low = mid + 1
    
    else:
        high = mid - 1
else:
    print(-1)



"""
Time Complexity: O(log(N)) (where N is the size of the given array)
In each step, the search space is divided into two halves. In the worst case, this process will continue until the search space can no longer be divided and the number of divisions required to reduce the array size to one is log(N), making the overall time complexity O(log(N)).

Space Complexity: O(1)
Using only a couple of variables.
"""