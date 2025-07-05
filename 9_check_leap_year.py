num = int(input("enter number:"))

if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("leap year")
else:
    print("Not leap year")