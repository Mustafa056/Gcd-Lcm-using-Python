def cal_Lcd(a, b):
    while (b != 0):
        rem = a % b
        a = b
        b = rem
    return a


a = int(input("num1:"))
b = int(input("num2:"))
print(f"Lcd is:{cal_Lcd(a, b)}")
t, c = a, b


def cal_lcm(t, c):
    return ((t * c) // cal_Lcd(a, b))


print(f"Lcm is {cal_lcm(t, c)}")
