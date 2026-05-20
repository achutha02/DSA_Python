"""Finding out the number at the given index"""

def pascalTriangle(r, c):
    return nCr(r-1, c-1)

def nCr(n, r):
    if r > n-r:
        r = n-r
    
    if r == 1:
        return n
    
    res = 1

    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    
    return res

print(pascalTriangle(5, 3))



"""
Time Complexity: O(C), where C is the column number. This is because the loop in the nCr function runs for a total of C times, where C can be as large as N/2.

Space Complexity: O(1), as no extra space is used.
"""
