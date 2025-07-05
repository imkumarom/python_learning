num1 = int(input("enter number:"))
num2 = int(input("enter number:"))
num3 = int(input("enter number:"))

if num1 >= num3 and num2 >= num3:
    print(f"greatest number is:{num1}")
elif num3 >= num2 and num2 >= num1:
    print(f"gretest number is:{num2}")
else:
    print(f"gretest number is:{num3}")