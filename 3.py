# 📍 Программа, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('✏️  Введите X: '))
y = int(input('✏️  Введите Y: '))
if x == 0 or y == 0:
    print('❌ Оба числа НЕ должны быть равны 0 !')
elif x > 0 and y > 0:
    print('Число в 1 четверти')
elif x < 0 and y > 0:
    print('Число в 2 четверти')
elif x < 0 and y < 0:
    print('Число в 3 четверти')
else:
    print('Число в 4 четверти')