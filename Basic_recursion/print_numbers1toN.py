def print_1toN(i,n):
    if i > n:
        return
    
    print(i, end=" ")
    print_1toN(i+1,n)

print_1toN(1,5)


# Tail Recursion (Work Happens Before Recursion)