sides_list = input('Triangle sides: ').split(' ')

# var 1
L = [float(el) for el in sides_list]
cond_1 = L[0] + L[1] > L[2]
cond_2 = L[1] + L[2] > L[0]
cond_3 = L[2] + L[0] > L[1]

if cond_1 and cond_2 and cond_3:
    print('OK')
else:
    print('Not OK')

# Var 2 \
cond = 1
L = [float(el) for el in sides_list]
for i in range(len(L)):
    cond *= int(L[0]+L[1] > L[2])
    L.insert(0, L[2])
    L.pop()
if cond == 1:
    print('OK')
else:
    print('Not OK')
