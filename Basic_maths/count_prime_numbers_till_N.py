import math

n = int(input("Enter a number: "))


count = 0

for num in range(2, n + 1):
    count1 = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count1 += 1

            if num // i != i:
                count1 += 1
        
    if count1 == 2:
        count += 1

print(count)
        
    
    

