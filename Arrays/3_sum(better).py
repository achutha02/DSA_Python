arr = [-1, 0, 1, 2, -1, -4]

n = len(arr)

triplet_set = set()

for i in range(n):
    hashset = set()
    for j in range(i+1, n):
        third = -(arr[i] + arr[j])

        if third in hashset:
            temp = [arr[i], arr[j], third]

            temp.sort()

            triplet_set.add(tuple(temp))
        
        hashset.add(arr[j])

ans = [list(triplet) for triplet in triplet_set]

print(ans)




"""
Time Complexity:  O(N^2 x log(no. of unique triplets)), where N is size of the array.
Inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. However, we are not considering the time complexity of sorting, as we are only sorting 3 elements each time.


Space Complexity: O(2 x no. of the unique triplets) + O(N) for using a set data structure and a list to store the triplets and extra O(N) for storing the array elements in another set.
"""