def printNto1(n):
    if n == 0:
        return
    
    print(n, end=" ")
    printNto1(n-1)

printNto1(5)

# Printing N to 1 (Using Tail Recursion)