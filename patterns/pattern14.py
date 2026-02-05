import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    for j in range(ord('A'), ord('A')+i+1):
        print(chr(j), end=' ')
    
    print()

# ord('A') gives character to number. Gives ASCII value
# chr(j) gives number to character 