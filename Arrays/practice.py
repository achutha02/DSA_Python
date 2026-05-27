nums = [1, -2, 3, 5, 7, 9]

n = len(nums)

ans = []

st = set()

target = 7

for i in range(n):
    for j in range(i+1, n):
        hashset = set()

        for k in range(j+1, n):
            curr_sum = nums[i] + nums[j] + nums[k]
            fourth = target - curr_sum

            if fourth in hashset:
                temp = [nums[i], nums[j], nums[k], fourth]

                temp.sort()
                st.add(tuple(temp))
            
            hashset.add(nums[k])

ans = [list(t) for t in st]
print(ans)


    
