# #แบบ 1

# # for i in range(5):
# #     print(i)


# #แบบ 2

# r = range(5)
# for i in r:
#     print(i)

#แบบ 3 start stop
for i in range(1, 6):
    print(i)

#แบบ 4 start stop step +

for i in range (10,20,2):
    print(i)

#แบบ 5 start stop step -
for i in range (15,1,-3):
    print(i)

# for วนรอบข้อมูลแบบลำดับได้ เช่น list, tuple, string, dictionary
s = 'Python' 
for i in s:
    print(i)

num = '12345'
sum = 0
for i in num:
    sum += int(i)
    print(sum)
