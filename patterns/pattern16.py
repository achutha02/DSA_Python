import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    ch = ord('A')+i
    for j in range(i+1):
        print(chr(ch), end=' ')
    
    print()