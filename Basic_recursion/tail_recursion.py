def tail_recursion(n):
    if n == 0:
        return
    
    print(n, end=" ")
    tail_recursion(n-1)

tail_recursion(5)