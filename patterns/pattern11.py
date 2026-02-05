import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    if i%2 == 0:
        start = 1
    else:
        start = 0
    
    for j in range(i+1):
        print(start, end=" ")
        start = 1 - start
    
    print()
