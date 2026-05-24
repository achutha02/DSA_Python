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