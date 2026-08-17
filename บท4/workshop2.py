#Workshop 4_2

num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
num3 = int(input('Enter number 3 : '))
if num1 > num2:
    if num1 > num3:
        max = num1
    else:
        max = num3
else:
    if num2 > num3:
        max = num2
    else:
        max = num3
print("Maximum number : ",max)
