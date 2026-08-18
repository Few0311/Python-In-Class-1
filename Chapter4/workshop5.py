#Workshop 4_5

#การรับค่าตัวเลขจากผู้ใช้ และตรวจสอบว่าตัวเลขนั้นเป็นเลขคู่หรือเลขคี่

num = int(input("Enter max number : "))
for i in range (1,num+1):
    if i % 2 == 0:
        print(f'{i} is even number ')
    else:
        print(f'{i} is odd number ')