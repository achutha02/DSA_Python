n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

lcm = 0
i = 1
n = max(n1,n2)

while True:
    mul = n * i
    if mul % n1 == 0 and mul % n2 == 0:
        lcm = mul
        break
    i = i + 1

print(lcm)