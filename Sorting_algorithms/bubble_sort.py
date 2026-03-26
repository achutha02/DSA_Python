arr  = [13, 46, 24, 52, 20, 9]

n = len(arr)

for i in range(n-1, 0, -1):
    isSwapped = False
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            isSwapped = True
        
    if not isSwapped:
        break

for ele in arr:
    print(ele, end=" ")