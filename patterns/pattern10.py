import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    for j in range(i+1):
        print("*", end='')
    
    print()

for i in range(n):
    for j in range(n-i-1):
        print("*", end='')
    
    print()



# Another method

for i in range(1, 2*n):
    stars = i if i<=n else 2*n-i
    for j in range(1, stars+1):
        print("*", end='')

    print()