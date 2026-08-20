nums = [5, 7, 7, 8, 8, 10]
target = 8

n = len(nums)

first = -1
last = -1

for i in range(n):
    if nums[i] == target:
        if first == -1:
            first = i

        last = i

print(first, last)