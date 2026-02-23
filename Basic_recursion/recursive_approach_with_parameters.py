def x_n_times(x, n):
    if n == 0:
        return
    
    print(x, end=" ")
    x_n_times(x, n-1)

x_n_times(4,5)