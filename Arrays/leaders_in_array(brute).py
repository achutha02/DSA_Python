nums = [10, 22, 12, 3, 0, 6]

n = len(nums)

ans = []

for i in range(n):
    leaders = True
    for j in range(i+1,n):
        if nums[j] >= nums[i]:
            leaders = False
            break
    
    if leaders:
        ans.append(nums[i])

print(ans)



"""
Time Complexity: O(N2), where N is the length of that array, as 2 nested for loops are used to traverse the array.

Space Complexity: O(1), as extra space to store answer is not considered.
"""