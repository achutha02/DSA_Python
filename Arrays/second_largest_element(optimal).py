arr = [1, 2, 4, 7, 7, 5]

largest = float('-inf')
second_largest = float('-inf')

if len(arr) < 2:
    print(-1)

else:
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        print(-1)
    
    else:
        print(second_largest)


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
