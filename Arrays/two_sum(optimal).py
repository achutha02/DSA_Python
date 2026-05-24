nums = [2, 6, 5, 8, 11]

target = 14

ans = [-1, -1]

n = len(nums)

eleIndex = []

for i in range(n):
    eleIndex.append([nums[i], i])


eleIndex.sort(key=lambda x:x[0])

left = 0
right = n-1

while left < right:
    curr_sum = eleIndex[left][0] + eleIndex[right][0]

    if curr_sum == target:
        ans[0] = eleIndex[left][1]
        ans[1] = eleIndex[right][1]
        break
    
    elif curr_sum < target:
        left += 1
    
    else:
        right -= 1

print(ans)
