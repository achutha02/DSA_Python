import sys


sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    
    for k in range(2*i+1):
        print("*", end='')
    
    print()

for i in range(n):
    for j in range(i):
        print(" ", end='')
    
    for k in range(2*n-(2*i+1)):
        print("*", end='')
    
    print()


# Another way
def erected_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end='')
        
        for k in range(2*i+1):
            print("*", end='')
        
        print()

def inverted_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ", end='')
        
        for k in range(2*n-(2*i+1)):
            print("*", end='')
        
        print()

def pattern9(n):
    erected_pyramid(n)
    inverted_pyramid(n)

pattern9(5)
