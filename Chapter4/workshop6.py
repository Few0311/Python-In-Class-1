#WorkShop 4_6

total = 0.0
Max = int(input("Enter number of score : "))
for i in range(1,Max+1):
    score = float(input("Enter score #"+str(i)+": "))
    total = total + score
print()
print("Total score value : ",total)
print("Average score : ",total/Max)

#การรับค่าตัวเลขจากผู้ใช้ และคำนวณหาผลรวมและค่าเฉลี่ยของตัวเลขที่รับเข้ามา