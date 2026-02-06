import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

iniS = 0

for i in range(n):
    print("*"*(n-i), end='')

    print(" "*iniS, end='')

    print("*"*(n-i), end='')

    print()

    iniS +=2

iniS1 = 2*n-2

for i in range(n):
    print("*"* (i+1), end='')

    print(" "*iniS1, end='')

    print("*"* (i+1), end='')

    print()

    iniS1 -= 2