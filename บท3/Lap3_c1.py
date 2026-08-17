# Exercise 3 ทำ ตู้ ATM
withdraw = int(input("Enter number money withdraw : "))

# คำนวณแบงก์ 1000
cash1 = float(withdraw // 1000)

# หาเงินส่วนที่เหลือจากแบงก์ 1000 แล้วนำมาหาจำนวนแบงก์ 500
remainder = withdraw % 1000
cash2 = float(remainder // 500)

# หาเงินส่วนที่เหลือจากแบงก์ 500 แล้วนำมาหาจำนวนแบงก์ 100
remainder = remainder % 500
cash3 = float(remainder // 100)

print("Cash B1000 :", cash1)
print("Cash B500  :", cash2)
print("Cash B100  :", cash3)

 
