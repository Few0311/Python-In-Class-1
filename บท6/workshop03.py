# Workshop 6_3
total = 0.0
for i in range(1,5):
    point = int(input(f'Enter point grade {i} (0-4) : '))
    total += point
credite = 4
gpa = total / credite
print()
print("You have %d subject " % credite)
print("You have total point = %5.2f , %d credite" % (total , credite))
print("You get gpa = %5.2f" % gpa )

#การจัดรูปแบบ print(f'') {}
name = 'Nuttapol'
salary = 25200.566
number = 3500
print(f'|{name}|{salary}|{number}|')
print(f'|{name:10}|{salary:12}|{number:8}|')
print(f'|{name:10}|{salary:12.2f}|{number:8}')
print(f'|{name:10}|{salary:12,}|{number:8,}')

