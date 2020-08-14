# 3. Дан список. Найти произведение (перемножить) всех элементов списка.

some_list = [2, 3, 4.6, 67, -1, 0.5, 6.01]

# Var 1.
prod = 1
for i in range(len(some_list)):
    prod *= some_list[i]
print('List product: {}'.format(str(prod)))

# Var 2.
prod = 1
while len(some_list) > 0:
    prod *= some_list.pop(0)
print('List product: {}'.format(str(prod)))
