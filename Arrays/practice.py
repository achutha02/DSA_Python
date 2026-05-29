nums = [2, 3, 5, -2, 7, -4]

n = len(nums)

max_sum = 0

for i in range(n):
    sum = 0
    for j in range(n):
        sum += nums[j]

        if sum > max_sum:
            max_sum = sum

print(max_sum)


    
