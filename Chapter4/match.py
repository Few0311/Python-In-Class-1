# d = 2 
# match d:
#     case 0:
#         print("0")
#     case 1:
#         print("1")
#     case 2:
#         print("Hello")
#     case _:
#         print('other')

#match case คือการใช้โครงสร้างการควบคุมแบบใหม่ใน Python 3.10 ขึ้นไป 
# ซึ่งช่วยให้สามารถตรวจสอบค่าของตัวแปรและทำงานตามกรณีที่ตรงกับค่าที่กำหนดได้อย่างง่ายดาย โดยไม่ต้องใช้หลาย ๆ if-elif-else เหมือนในตัวอย่างก่อนหน้านี้

score = 67
match score:
    case score if 80 <= score <= 100:
        print('A')
    case score if 70 <= score < 80:
        print('B')
    case score if 60 <= score < 70:
        print('C')
    case score if 50 <= score < 60:
        print('D')
    case score if 0 <= score < 50:
        print('F')
    case _:
        print("Score not in range.")