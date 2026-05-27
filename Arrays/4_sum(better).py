nums = [1, -2, 3, 5, 7, 9]

target = 7

ans = []

st = set()

n = len(nums)

for i in range(n):
    for j in range(i + 1, n):

        hashset = set()

        for k in range(j + 1, n):

            current_sum = nums[i] + nums[j] + nums[k]

            fourth = target - current_sum

            if fourth in hashset:

                temp = [nums[i], nums[j], nums[k], fourth]

                temp.sort()

                st.add(tuple(temp))

            hashset.add(nums[k])

ans = [list(t) for t in st]

print(ans)




"""
Time Complexity:  O(N^3xlog(M)), for using 3 nested loops and inside the loops there are some operations on the set data structure which take log(M) time complexity, where N is size of the array, M is number of elements in the set.


Space Complexity: O(2 x no. of the quadruplets)+O(N) for using a set data structure and a list to store the quads. This results in the first term. And the second space is taken by the set data structure we are using to store the array elements. At most, the set can contain approximately all the array elements and so the space complexity is O(N).
"""
