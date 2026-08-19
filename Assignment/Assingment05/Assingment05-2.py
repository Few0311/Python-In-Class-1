print("=== ระบบคำนวณเงินหน้าร้าน(POS)===")
price = int(input("กรุณากรอกราคารวมสินค้าทั้งหมด(บาท): "))
member = input("ลูกค้าเป็นสมาชิกหรือไม่ (y/n):") == "y"
print()
space1,space2 = "-"*34,"="*34
#เช็คเงื่อนไขส่วนลด 
if price <= 1000: discount1 = 0
elif price <= 5000: discount1 = 2.5
elif price <= 10000: discount1 = 5
elif price <= 20000: discount1 = 7.5
else: discount1 = 10
#
discount_member = 5 if member else 0 
discount_all = discount1 + discount_member

discount_allmember = price * (discount_member/100)  #ส่วนเฉพาะลดจากสมาชิก
discount_product = price * (discount1/100) # ส่วนลดของราคาสินค้า
total_discount =  discount_allmember + discount_product  #ผลรวมส่วนลดทั้งหมด
total_price = price - total_discount #ราคาที่ต้องจ่ายจริง

print(f"{space1}\nส่วนลดที่ได้รับรวม: {discount_all:.1f}% ({total_discount:,.2f} บาท)")
print(f"จำนวนเงินที่ต้องจ่ายจริง: {total_price:,.2f} บาท\n{space1}")
#รับเงิน
Receive_payment = int(input("รับเงินจากลูกค้า (บาท): "))
print()
print(f"{space2}\n  สรุปการชำระเงิน\n{space2}")
print(f"ราคารวมสินค้า :  {price:,.2f} บาท")
print(f"ส่วนลดตามยอดซื้อ ({discount1:.1f}%): {discount_product:.2f} บาท\nส่วนลดสมาชิก  ({discount_member:.1f}%): {discount_allmember:,.2f} บาท")
print(f"ส่วนลดรวมทั้งหมด : {total_discount:,.2f} บาท\n{space1}\nยอดเงินที่ต้องจ่ายจริง : {total_price:,.2f} บาท\nจำนวนเงินที่รับมา : {Receive_payment:,.2f} บาท")
print(f"จำนวนเงินทอน : {Receive_payment - total_price:,.2f} บาท")
