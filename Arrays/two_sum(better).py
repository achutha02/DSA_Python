nums = [2, 6, 5, 8, 11]

target = 14

n = len(nums)

found = False

mpp = {}

for i in range(n):
    num = nums[i]

    more_needed = target - num

    if more_needed in mpp:
        print(mpp[more_needed],i)
        found = True
        break

    mpp[num] = i

if not found:
    print(-1, -1)