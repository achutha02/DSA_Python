import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

nums = [1,2,3,4,5,5,6,7,8,9,10]
print(nums)
for items in nums:
    print(items)