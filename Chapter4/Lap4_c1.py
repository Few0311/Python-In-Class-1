# Exercise 4

print(">>Program Find Maximum Digit<<")

# 1. รับค่าครั้งแรกก่อนเข้าลูป
num = int(input("Enter integer number(0-exit) : "))

# 2. วนลูปทำงานตราบใดที่ num ไม่เท่ากับ 0
while num != 0:
    maxDigit = 0
    temp = num  # สำรองค่า num ไว้ใช้คำนวณแยกหลัก

    # ลูปหาเลขโดดที่มากที่สุด
    while temp > 0:
        digit = temp % 10
        if digit > maxDigit:
            maxDigit = digit
        temp = temp // 10

    print(f"Maximum Digit of integer number {num} = {maxDigit}")

    # รับค่าตัวเลขตัวถัดไป
    num = int(input("Enter integer number(0-exit) : "))

print("Exit Program")

    
