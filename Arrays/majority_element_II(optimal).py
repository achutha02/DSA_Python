nums = [2, 1, 1, 3, 1, 4, 5, 6]

n = len(nums)

cnt1 = 0
cnt2 = 0

el1 = float('-inf')
el2 = float('-inf')

for i in range(n):
    if cnt1 == 0 and nums[i] != el2:
        cnt1 = 1
        el1 = nums[i]
    
    elif cnt2 == 0 and nums[i] != el1:
        cnt2 = 1
        el2 = nums[i]
    
    elif nums[i] == el1:
        cnt1 += 1
    
    elif nums[i] == el2:
        cnt2 += 1
    
    else:
        cnt1 -= 1
        cnt2 -= 1
    

cnt1 = 0
cnt2 = 0

for num in nums:
    if num == el1:
        cnt1 += 1
    
    elif num == el2:
        cnt2 += 1

result = []

mini = (n // 3) + 1

if cnt1 >= mini:
    result.append(el1)

if cnt2 >= mini and el2 != el1:
    result.append(el2)

print(result)




"""
Time Complexity: O(N) + O(N), where N is size of the given array. The first O(N) is to calculate the counts and find the expected majority elements. The second one is to check if the calculated elements are the majority ones or not.

Space Complexity: O(1) for only using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.
"""

