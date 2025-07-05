num = int(input("enter number:"))

fibbo = 0 and 1

fibbonaci = ("f(n) = f(n-1) + f(n-2)")

for i in range(0,1, num+1):
     if num % i == 1:
        fibbo = 1 + fibbo
     print(f"fibbonaci sequnce {num} is {fibbo}")