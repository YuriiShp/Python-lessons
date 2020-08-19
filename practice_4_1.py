#Var1
n_list = [1, 3, 4, 5, 4, 3, 34, 32, 0, 7]

n_sum = 0
for el in n_list:
    n_sum += el
print(n_sum)

#Var2
n_sum = 0
while n_list:
    n_sum += n_list.pop()
print(n_sum)

#Var3
n_list = [1, 3, 4, 5, 4, 3, 34, 32, 0, 7]


def arsum(n):
    if not n:
        return 0
    else:
        res = n.pop() + arsum(n)
        return res


n_sum = arsum(n_list)
print(n_sum)
