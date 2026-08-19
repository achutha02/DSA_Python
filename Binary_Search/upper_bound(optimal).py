nums = [3, 5, 8, 15, 19]

x = 3

n = len(nums)

low = 0
high = n-1

ans = n

while low <= high:
    mid = (low + high) // 2

    if nums[mid] > x:
        ans = mid
        high = mid - 1
    
    else:
        low = mid + 1

print(ans)
