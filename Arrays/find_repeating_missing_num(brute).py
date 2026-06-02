nums = [1, 2, 3, 6, 7, 5, 7]

n = len(nums)

repeating = -1
missing = -1

for i in range(1,n+1):
    cnt = 0
    for j in range(n):
        if nums[j] == i:
            cnt += 1
        
    
    if cnt == 2:
        repeating = i
    
    elif cnt == 0:
        missing = i
    
    if repeating != -1 and missing != -1:
        break

print([repeating, missing])



"""
Time Complexity: O(N^2), where N is the size of the array. Since we are using nested loops to count occurrences of every element between 1 to N.

Space Complexity: O(1) as no extra space is used.
"""