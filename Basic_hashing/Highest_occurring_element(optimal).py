arr = [4, 4, 5, 5, 6]

n = len(arr)

maxEle = 0

maxFreq = 0

mpp = {}

for i in range(n):
    if arr[i] in mpp:
        mpp[arr[i]] += 1
    
    else:
        mpp[arr[i]] = 1

for ele, freq in mpp.items():
    if freq > maxFreq:
        maxFreq = freq
        maxEle = ele
    
    elif freq == maxFreq:
        maxEle = min(maxEle, ele)

print(f"the max element is {maxEle}")

