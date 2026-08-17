#WorkShop 6_4  การจัดด้วย %

import math
print()
print("=" * 40 )
print("|Angle|  sin |   cos |   Tan |")
print("=" * 40  )
for angle in range(0, 361, 20):
    radian = math.radians(angle)
    print(f'|%4d |' % angle,end='')
    print('%9.5f |' % math.sin(radian),end='')
    print('%9.5f |' % math.cos(radian),end='')
    print('%9.5f |' % math.tan(radian))
print("=" * 40)


#การจัดด้วย f'{}'
print()
print('=' * 40)
print('|Angle|  sin |   cos |   Tan |')
print('=' * 40)
for angle in range(0, 361, 20):
    radian = math.radians(angle)
    print(f'|{angle:4} |',end='')
    print(f'{math.sin(radian):9.5f} |',end='')
    print(f'{math.cos(radian):9.5f} |',end='')
    print(f'{math.tan(radian):9.5f} |')
print('=' * 40)

