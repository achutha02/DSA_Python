arr = [4, 4, 5, 5, 6]

n = len(arr)

maxEle = 0

maxFreq = 0

visited = [False] * n

for i in range(n):
    freq = 0

    if visited[i]:
        continue

    for j in range(i,n):
        if arr[i] == arr[j]:
            freq += 1
            visited[i] = True
        
    if freq > maxFreq:
        maxFreq = freq
        maxEle = arr[i]
        
    elif freq == maxFreq:
        maxEle = min(maxEle, arr[i])

print(f"The max element is {maxEle}")
