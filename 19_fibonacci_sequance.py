num = int(input("enter number:"))

a = 0
b = 1

print(f"fibonacci sequence of first {num} is:")

for i in range(500):
    if a > num:
        break
    print(a, end =" ")
    tmp = a 
    a=b
    b=tmp+b
19_fibonacci_sequance.py