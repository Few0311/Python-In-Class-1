# # WorkShop 4_8

total = 0.0
score = 1 
count = 0
while score > 0:
    score = int(input("Enter score value #"+str(count+1)+": "))
    if score > 0:
        count += 1
        total += score

print()
print("Number of score : ",count)
print("total score value : ",total)
print("Average score : ",total/count)

#การรับค่าตัวเลขจากผู้ใช้ และคำนวณหาผลรวมและค่าเฉลี่ยของตัวเลขที่รับเข้ามา โดยจะหยุดรับค่าตัวเลขเมื่อผู้ใช้ป้อนค่าติดลบหรือศูนย์


#pass statement เป็นคำสั่งที่ใช้เพื่อบอกให้โปรแกรมทำงานต่อไป โดยไม่ทำอะไรเลย


# s = 51
# if s >= 50:
#     print(" You Pass ")
# else:
#     pass

#break statement เป็นคำสั่งที่ใช้เพื่อบอกให้โปรแกรมหยุดการทำงานของ loop และออกจาก loop นั้นทันที


# for i in range(1,10):
#     if i == 6:
#         break
#     print(i)
#continue statement เป็นคำสั่งที่ใช้เพื่อบอกให้โปรแกรมข้ามการทำงานของ loop ในรอบนั้น และไปทำงานต่อในรอบถัดไป

# for i in range(1,10):
#     if i == 4 or i == 8:
#         continue
#     print(i)