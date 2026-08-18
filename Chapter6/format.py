#การจัดรูปแบบการแสดงผล (Format)
name = 'Python'
print('%s' % name)
# %s จำนวนสตริง
name = 'Python'
print('|%s|' % name)
print('|%10s|' % name)
print('|%-10s|' % name)
print('|%-10c|' % name[0])
print('|%10c|' % name[0])

 # %d จำนวนเต็ม
num = 8 
print('|%d|' % num)
print('|%3d|' % num)
print('|%-3d' % num)
print('|%03d' % num)
print('|%-03d' % num)

# %f จำนวนทศนิยม
gpa = 2.9580
print('|%f' % gpa)
print('|%d|' % gpa)
print('|%.2f|' % gpa)
print('|%5.2f| ' % gpa)
print('|%7.3f|' % gpa)
print('|%07.3f|' % gpa)




