# 2. Пользователь вводит строку и символ (одну букву). Проверить есть ли в этой строке введенный символ.

some_str = input('Input text: ')
some_symbol = input('Searching symbol: ')

# Var 1.
some_set = set(some_str)
n_of_steps = len(some_set)
while n_of_steps > 0:
    if some_symbol == some_set.pop():
        print('symbol {} is in string {}'.format(some_symbol, some_str))
        break
    n_of_steps -= 1
    if n_of_steps == 0:
        print('symbol {} not found'.format(some_symbol))

# Var 2.
if some_symbol in some_str:
    print('symbol {} is in string {}'.format(some_symbol, some_str))
else:
    print('symbol {} not found'.format(some_symbol))
