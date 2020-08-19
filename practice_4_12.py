money = int(input('Amount of money: '))

b500 = 0
b100 = 0
b10 = 0
b2 = 0

if money >= 500:
    b500 = money // 500
    money = money % 500
if money >= 100:
    b100 = money // 100
    money = money % 100
if money >= 10:
    b10 = money // 10
    money = money % 10
if money >= 2:
    b2 = money // 2
    money = money % 2

print('500: {} / 100: {} / 10: {} / 2: {}'.format(b500, b100, b10, b2))
