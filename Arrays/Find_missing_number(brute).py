nums = [0, 1, 2, 4]

n = len(nums)

found_mising = False

for i in range(n):
    flag = 0
    for j in range(n):
        if nums[j] == i:
            flag = 1
    
    if flag == 0:
        print(i)
        found_mising = True

if not found_mising:
    print(-1)