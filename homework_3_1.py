# 1. Дан список чисел. Необходимо вывести в отдельные списки (три списка пустых) такие числа:
# в первый добавляем все числа которые делятся на 2
# во второй - те которые делятся на три
# в третий - те которые не подходят под первые два условия

some_list = [1, 2, 3, 4, 5, 6, 8, 98, 54, 34, -7, 0]
div_by_2 = []
div_by_3 = []
other_num = []

for el in some_list:
    if el % 2 == 0:
        div_by_2.append(el)
    if el % 3 == 0:
        div_by_3.append(el)
    if not(el % 2 == 0 or el % 3 == 0):
        other_num.append(el)
print('Numbers div by 2: {}'.format(str(div_by_2)))
print('Numbers div by 3: {}'.format(str(div_by_3)))
print('Other numbers: {}'.format(str(other_num)))

