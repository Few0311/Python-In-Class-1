#Exercise 4_2

print(">>Program Find Maximum Value <<")
num = int(input("Enter number of value(>=1) : "))
if num >= 1:
    print("Program get value ",num,"number")
    value = 0
    maxvalue = 0
    all_number = ""
    for i in range(1,num+1):
        value = int(input("Enter value Number #" + str(i) + " : "))
        all_number += str(value) + " "
        if value > maxvalue:
            maxvalue = value 
    print("Your enter number :",all_number)
    print("Maximum value number is : ",maxvalue)
else:
    print("value input not correct")
print("Exit Program")

#โปรแกรมรับค่าตัวเลขจากผู้ใช้จำนวน n ตัว และหาค่าตัวเลขที่มากที่สุดจากตัวเลขที่รับเข้ามา
