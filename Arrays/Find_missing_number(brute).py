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


"""
Time Complexity: O(N^2), where N is the size of the array. In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single number the inner loop will also run for approximately N times. So, the total time complexity will be O(N^2).

Space Complexity: O(1)
"""