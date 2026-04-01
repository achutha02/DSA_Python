nums = [1, 1, 0, 0, 1, 1, 1, 0]

count = 0
largest_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        count += 1

        largest_count = max(largest_count, count) # Or using if condition
    
    else:
        count = 0

print(largest_count)



"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
