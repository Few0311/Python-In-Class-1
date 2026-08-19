# นาย ณัฏฐำพล พรเลิศ 6906021611447

number = int(input(f"{" "*5}กรอกแม่สูตรคูณแม่ (2-12): "))
if 2 <= number <= 12:
    print(f"{" "*8}ตารางสูตรคูณ {number}")
    print(f"{"-"*32}")
    for i in range(1, 13, +1):
        print(f"{" "*10}{number} x {i} = {i*number}")
else:
    print("กรุณากรอกเลขระหว่าง 2 ถึง 12")
    