# 3. Напишите программу которая просит пользователя ввести число и проверяет есть ли это число в массиве.
# Массив взять произвольный.
arr = [3, 5, 67, 6.8, 21, 0, 55, 419, 3]
inp_num = float(input('Input number: '))
if arr.count(inp_num) != 0:
    print('OK')
