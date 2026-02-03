import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

for i in range(0,5):
    print(f"value of i {i}")
    print()
    for j in range(0,5):
        print(f"value of j {j}")
    print()
