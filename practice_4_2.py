list_a = [1, 2, 3]
list_b = [11, 22, 33]
list_ab = []

for i in range(len(list_a)):
    list_ab.extend([list_a[i], list_b[i]])
print(list_ab)
