nums = [3, 5, 8, 15, 19]

x = 3

n = len(nums)

ans = n

for i in range(n):
    if nums[i] > x:
        ans = i
        break

print(ans)



"""
Time Complexity: O(N), where N is the size of the given array. In the worst case, we have to traverse the entire array, which is the time complexity of the linear search algorithm.

Space Complexity: O(1), as we are using no extra space to solve this problem.
"""
    
