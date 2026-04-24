nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

n = len(nums)

max_cnt = -1

for i in range(n):
    cnt = 0
    for j in range(n):
        if nums[j] == nums[i]:
            cnt += 1
    
    if cnt > (n//2):
        max_cnt = nums[i]
        break

print(max_cnt)




'''
Time Complexity:  O(N2), for nested for loops used, where N is the size of the array

Space Complexity: O(1) as no extra space is used.
'''