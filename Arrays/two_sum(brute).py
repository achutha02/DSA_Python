nums = [2, 6, 5, 8, 11]

target = 14

is_true = False

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            is_true = True
            print(i, j)
            break

if not is_true:
    print(-1,-1)
