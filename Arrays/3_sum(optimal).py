nums = [-1, 0, 1, 2, -1, -4]

n = len(nums)

ans = []

nums.sort()

for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue

    j = i+1
    k = n-1

    while j < k:
        sum_val = nums[i] + nums[j] + nums[k]

        if sum_val < 0:
            j += 1
        
        elif sum_val > 0:
            k -= 1
        
        else:
            temp = [nums[i], nums[j], nums[k]]
            ans.append(temp)

            j += 1
            k -= 1

            while j < k and nums[j] == nums[j-1]:
                j += 1
            
            while j < k and nums[k] == nums[k+1]:
                k -= 1
    
print(ans)





"""
Time Complexity:  O(NlogN)+O(N^2), where N is size of the array. As the pointer i, is running for approximately N times. And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N^2).


Space Complexity: O(1), no extra space is used.
"""