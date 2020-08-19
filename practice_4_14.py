N = int(input('Input number: '))
ab = [int(el) for el in input('Input range: ').split('...')]

for i in range(ab[0], ab[1]+1):
    print('{} x {} = {};'.format(N, i, N*i))
