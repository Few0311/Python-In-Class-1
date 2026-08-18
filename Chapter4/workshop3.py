
score = int(input("Enter  score : "))
if score <= 0:
    print("Score not in range. ")
elif score > 100:
    print("Score not in range.")
else:
    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    elif score <= 49:
        grade = 'F'
print('Score value ',score,'got grade',grade)
    



