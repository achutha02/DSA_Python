import math

n = int(input("Enter a number: "))

sum = 0

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        sum = sum + i
    
        if (n // i)!= i and (n // i)!= n:
            sum = sum + (n // i)

if sum == n:
    print("The number is perfect number")

else:
    print("The number is not perfect number")