a_range = [int(el) for el in input('A range: ').split(' ')]
b_range = [int(el) for el in input('B range: ').split(' ')]
c_range = [int(el) for el in input('C range: ').split(' ')]


for a in range(a_range[0], a_range[1]+1):
    for b in range(b_range[0], b_range[1] + 1):
        for c in range(c_range[0], c_range[1] + 1):
            D = b**2 - 4 * a * c
            if D > 0:
                print('a = {}, b = {}, c = {}: 2 roots'.format(a, b, c))
            elif D == 0:
                print('a = {}, b = {}, c = {}: 1 root'.format(a, b, c))
            else:
                print('a = {}, b = {}, c = {}: 0 roots'.format(a, b, c))
