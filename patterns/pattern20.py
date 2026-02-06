import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')


n = int(input())

iniS = 2*n-2

for i in range(n):
    print("*"* (i+1), end='')

    print(" "*iniS, end='')

    print("*"* (i+1), end='')

    print()

    iniS -= 2

iniS1 = 2

for i in range(1,n):
    print("*" * (n-i), end='')

    print(" "*iniS1, end='')

    print("*" * (n-i), end='')

    print()

    iniS1 += 2




# Another method

spaces = 2 * n - 2

for i in range(1, 2*n):
    if i < n:
        stars = i
    else:
        stars = 2 * n - i
    print("*" * stars, end='')

    print(" " * spaces, end='')

    print("*"* stars, end='')

    print()

    if i<n:
        spaces -= 2
    
    else:
        spaces += 2