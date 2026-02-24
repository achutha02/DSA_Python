def isPrime(num):
    if num <= 1:
        return False
    return prime(num, 2)

def prime(num, x):
    if x > num ** 0.5:
        return True
    
    if num % x == 0:
        return False
    
    return prime(num, x+1)

print(isPrime(7))