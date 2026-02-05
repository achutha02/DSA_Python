import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    for j in range(ord('A'), ord('A')+n-i):
        print(chr(j), end=' ')
    
    print()