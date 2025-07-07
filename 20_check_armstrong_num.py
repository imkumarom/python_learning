
for num in range(1,1000000001):
    actual_no=num
    cube_sum_val=0
    power=len(str(num))

    while (num>0):
        last_dist=num%10
        cube_sum_val=last_dist ** power + cube_sum_val
        num=int(num/10)

    if actual_no==cube_sum_val:
        print(f"{actual_no} number is armstrong")
# else:
#     print(f"{actual_no} number is not armstrong")