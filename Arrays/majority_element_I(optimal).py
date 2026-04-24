nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

n = len(nums)

cnt = 0

el = 0

for num in nums:
    if cnt == 0:
        cnt = 1
        el = num
    
    elif el == num:
        cnt += 1
    
    else:
        cnt -= 1

cnt1 = nums.count(el)

if cnt1 > (n//2):
    print(el)

else:
    print(-1)


"""
Time Complexity: O(N) + O(N), where N is size of the given array. The first O(N) is to calculate the count and find the expected majority element. The second one is to check if the expected element is the majority one or not.

Space Complexity: O(1) no extra space used.


This is also called Boyer-Moore Voting Algorithm
"""