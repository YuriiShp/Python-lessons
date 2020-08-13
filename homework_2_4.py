# 4. Такая же как и 3, но проверяем есть ли такой ключ в словаре. Словарь так же произвольный.
dict_a = {'name': 'Oleg', 'age': 25, 'education': 'higher'}
inp_key = input('Input key: ')
if dict_a.get(inp_key, 'none') != 'none':
    print(dict_a.get(inp_key))
else:
    print('key does not exist')