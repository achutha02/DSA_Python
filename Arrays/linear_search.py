nums = [2, 3, 4, 5, 3]
target = 3

n = len(nums)
found = False

for i in range(n):
    if nums[i] == target:
        print(i)
        found = True
        break

if not found:
    print(-1)
