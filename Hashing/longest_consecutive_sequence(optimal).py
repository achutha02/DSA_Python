nums = [100, 4, 200, 1, 3, 2]

n = len(nums)

longest = 1
st = set()

if n == 0:
    print(0)
else:
    for i in range(n):
        st.add(nums[i])
    
    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it

            while x + 1 in st:
                x += 1
                cnt += 1
        
        longest = max(longest, cnt)


print(longest)



"""
Time Complexity: O(N) + O(2xN) ~ O(3xN), where N is the size of the array. The function takes O(N) to insert all elements into the set data structure. After that, for every starting element, we find the consecutive elements. Although nested loops are used, the set will be traversed at most twice in the worst case. Therefore, the time complexity is O(2xN) instead of O(N^2).

Space Complexity: O(N), as we use a set data structure to solve this problem.
"""