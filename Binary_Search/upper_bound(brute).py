nums = [3, 5, 8, 15, 19]

x = 3

n = len(nums)

ans = n

for i in range(n):
    if nums[i] > x:
        ans = i
        break

print(ans)
    
