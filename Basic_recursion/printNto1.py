def printNto1(i,n):
    if i > n:
        return
    
    printNto1(i+1,n)
    print(i, end=" ")

printNto1(1,5)

# Printing N to 1 (Using Head Recursion)