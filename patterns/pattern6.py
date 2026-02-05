import sys
import bisect

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    for j in range(n-i):
        print(j+1, end='')
    print()