import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    
    ch = 'A'
    br = (2*i+1) // 2
    for k in range(1, 2*i+2):
        print(ch, end='')
        if k <= br:
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)
    
    print()