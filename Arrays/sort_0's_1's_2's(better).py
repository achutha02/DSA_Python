nums = [1, 0, 2, 1, 0]

n = len(nums)

cnt0 = 0
cnt1 = 0
cnt2 = 0

for num in nums:
    if num == 0:
        cnt0 += 1
    elif num == 1:
        cnt1 += 1
    
    else:
        cnt2 += 1

for i in range(cnt0):
    nums[i] = 0

for i in range(cnt0, cnt0 + cnt1):
    nums[i] = 1

for i in range(cnt0 + cnt1, n):
    nums[i] = 2

print(nums)




"""
Time Complexity: O(N)+O(N) = O(2N), where N is the size of the array. There are 2 traversals in the array to count the frequencies then in second iteration we are overwriting.

Space Complexity: O(1) no extra space used.
"""