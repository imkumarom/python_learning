num = int(input("enter number:"))

om = 0

for i in range(1,num+1):
    if om % i == om:
        om = om + 1
