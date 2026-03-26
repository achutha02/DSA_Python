arr = [13,46, 24, 52, 20, 9]

n = len(arr)

for i in range(1,n):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
    
for i in range(n):
    print(arr[i], end=" ")
