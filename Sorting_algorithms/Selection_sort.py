arr = [13, 56, 24, 52, 20, 9]
n = len(arr)

for i in range(n-1):
    mini_index = i
    for j in range(i+1,n):
        if arr[j] < arr[mini_index]:
            mini_index = j
    
    if mini_index != i:
        temp = arr[i]
        arr[i] = arr[mini_index]
        arr[mini_index] = temp

for i in range(n):
    print(arr[i], end=' ') 