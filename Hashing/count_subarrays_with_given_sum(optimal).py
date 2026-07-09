nums = [1, 1, 1]

k = 2

n = len(nums)

prefix_sum_map = {0:1}

current_sum = 0

subarray_count = 0

for i in range(n):
    current_sum += nums[i]

    sum_to_remove = current_sum - k

    subarray_count += prefix_sum_map.get(sum_to_remove, 0)

    prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0)+1

print(subarray_count)