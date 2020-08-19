r = [int(el) for el in input('Input range: ').split('...')]

all_n = list(range(r[0], r[1]+1))
init_list = all_n.copy()

not_prime = [el for el in all_n if (el % 2 == 0 and el != 2)\
             or (el % 5 == 0 and el != 5) or (el % 3 == 0 and el != 3)\
             or (el % 7 == 0 and el != 7)]
prime = []
while all_n:
    n = all_n.pop(0)
    if n not in not_prime:
        prime.append(n)

print(init_list)
print(not_prime)
print(prime)


