arr = [1, 2, 2, 3, 3, 3]

n = len(arr)

visited = [False] * n

max_freq = 0
min_freq = n

for i in range(n):
    freq = 0

    if visited[i]:
        continue

    for j in range(i, n):
        if arr[i] == arr[j]:
            freq += 1
            visited[j] = True
    
    max_freq = max(max_freq, freq)
    min_freq = min(min_freq, freq)

print(max_freq + min_freq)