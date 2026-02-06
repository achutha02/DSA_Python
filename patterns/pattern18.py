import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    for j in range(ord('A') + n-i-1, ord('A') + n):
        print(chr(j), end=' ')
        
    print()