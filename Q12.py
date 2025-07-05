num = int(input("enter number"))

om = 0

for i in range(1, num+1):
     if num % i == 0:
       om = om+1
if om > 2:
    print("not prime")
else:
    print("prime")