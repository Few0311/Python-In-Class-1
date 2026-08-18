#WorkShop 4_7

message = ""
maxValue = 5
count = 1 
while count <= maxValue:
    s = input("Enter string #"+str(count)+": ")
    message += s + "\n"
    count += 1

print("\nPrint your string enter : ")
print(message)

#การรับค่าตัวอักษรจากผู้ใช้ และเก็บค่าตัวอักษรที่รับเข้ามาในตัวแปร message
# += คือการนำค่าที่รับเข้ามาเก็บไว้ในตัวแปร message และต่อท้ายด้วยเครื่องหมาย \n เพื่อให้ขึ้นบรรทัดใหม่
