n1 = int(input("Enter a number: "))

n2 = int(input("Enter a number: "))

while(n1 > 0 and n2 > 0):
    if n1 > n2:
        n1 = n1 % n2
    
    else:
        n2 = n2 % n1


if(n2 == 0):
    print(n1)

else:
    print(n2)