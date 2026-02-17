arr = [10, 9, 7, 7]

n = len(arr)

maxFreq = 0
secMaxFreq = 0

maxEle = -1
secEle = -1

visited = [False] * n

for i in range(n):
    if visited[i]:
        continue
    
    freq = 0

    for j in range(i,n):
        if arr[i] == arr[j]:
            freq += 1
            visited[j] = True
        
    if freq > maxFreq:
        secMaxFreq = maxFreq
        secEle = maxEle
        maxFreq = freq
        maxEle = arr[i]
    
    elif freq == maxFreq:
        maxEle = min(maxEle, arr[i])
    
    elif freq > secMaxFreq:
        secMaxFreq = freq
        secEle = arr[i]
    
    elif freq == secMaxFreq:
        secEle = min(secEle, arr[i])

print(f"The second largest element is: {secEle}")



