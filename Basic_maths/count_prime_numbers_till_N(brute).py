def isPrime(n):
    count = 0

    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        return True
    return False

def primeCount(n):
    count = 0

    for i in range(2,n+1):
        if isPrime(i):
            count += 1
    
    return count

n = int(input("Enter a number: "))

print(primeCount(n))