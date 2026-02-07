n = int(input("Enter the number: "))

if n == 0:
    print("1")

cnt = 0
while(n>0):
    n = n // 10
    cnt = cnt + 1

print(cnt)