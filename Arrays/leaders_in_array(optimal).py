nums = [1, 2, 5, 3, 1, 2]

n = len(nums)

ans = []

if not nums:
    print(ans)

else:
    ans.append(nums[-1])
    maxi = nums[-1]

    for i in range(n-2,-1,-1):
        if nums[i] > maxi:
            ans.append(nums[i])
            maxi = nums[i]
            
    ans.reverse()
    print(ans)



"""
Time Complexity: O(N), for single traversal of array , where N is the length of that array.

Space Complexity: O(1), as extra space to store answer is not considered.
"""