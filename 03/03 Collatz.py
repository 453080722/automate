def collatz(number):
    global i
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number +1
    print("{}====={}".format(i, number))
    i += 1
    return number

number = input("请输入一个整数：")
i = 1
try:
    number = int(number)
except Exception as e:
    print(e)
    print("必须输入一个整数")

while number != 1:
    number = collatz(number)