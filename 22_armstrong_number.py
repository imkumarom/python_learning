num = int(input("enter a number:-"))

order = len(str(num))

sum_of_power = sum(int(digit) ** order for digit in str(num))

if num == sum_of_power:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")