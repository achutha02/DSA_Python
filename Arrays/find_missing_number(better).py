nums = [0, 2, 3, 1, 4]

n = len(nums)

freq = [0] * (n+1)

found_missing = False

for num in nums:
    freq[num] += 1

for i in range(n+1):
    if freq[i] == 0:
        print(i)
        found_missing = True

if not found_missing:
    print(-1)
