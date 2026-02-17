from collections import defaultdict

nums = [4, 4, 5, 5, 6, 7]

maxEle = -1
secEle = -1

maxFreq = 0
secMaxFreq = 0

mpp = defaultdict(int)

for num in nums:
    mpp[num] += 1

for ele, freq in mpp.items():
    if freq > maxFreq:
        secMaxFreq = maxFreq
        secEle = maxEle
        maxFreq = freq
        maxEle = ele
    
    elif freq == maxFreq:
        maxEle = min(maxEle, ele)
    
    elif freq > secMaxFreq:
        secMaxFreq = freq
        secEle = ele
    
    elif freq == secMaxFreq:
        secEle = min(secEle, ele)

print(f"the second element is: {secEle}")
