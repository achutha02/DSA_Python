nums = [2, -2, 0, 3, -3, 5]

n = len(nums)

triplet_set = set()

for i in range(n - 2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = [nums[i], nums[j], nums[k]]

                temp.sort()
                triplet_set.add(tuple(temp))

ans = [list(triplet) for triplet in triplet_set]

print(ans)