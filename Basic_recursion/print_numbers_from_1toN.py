def print1toN(n):
    if n == 0:
        return
    
    print1toN(n-1)
    print(n, end=" ")

print1toN(5)


# Head Recursion (Work Happens After Recursion)