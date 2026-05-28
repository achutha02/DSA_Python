nums = [1, -2, 3, 5, 7, 9]

target = 7

n = len(nums)

ans = []

nums.sort()

for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1, n):
        if j > i+1 and nums[j] == nums[j-1]:
            continue
        k = j+1
        l = n-1

        while k < l:
            sum_val = nums[i] + nums[j] + nums[k] + nums[l]

            if sum_val < target:
                k += 1
            
            elif sum_val > target:
                l -= 1
            
            else:
                temp = [nums[i], nums[j], nums[k], nums[l]]
                ans.append(temp)

                k += 1
                l -= 1

                while k < l and nums[k] == nums[k-1]:
                    k += 1
                
                while k < l and nums[l] == nums[l+1]:
                    l -= 1

print(ans)






"""
Time Complexity: O(N^3), where N is the size of the given array.
Sorting the array takes O(NlogN) time, and the 3 nested loops take O(N^3) time. Thus, the overall time complexity is O(N^3) + O(NlogN), which boils down to O(N^3).

Space Complexity: O(no. of quadruplets), this space is only used to store the answer. No extra space is used to solve this problem. So, from that perspective, space complexity can be written as O(1).
"""