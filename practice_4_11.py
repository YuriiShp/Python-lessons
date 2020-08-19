seat = int(input('Місце №: '))

if seat % 2 == 0:
    p_1 = 'верхнє'
else:
    p_1 = 'нижнє'

if seat > 36:
    p_2 = 'бокове'
else:
    p_2 = 'купейне'

if seat in range(35, 39):
    p_3 = 'біля туалету'
else:
    p_3 = ''

print('Місце №: {} - {} {} {}'.format(seat, p_1, p_2, p_3))
