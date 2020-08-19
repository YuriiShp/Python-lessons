n = int(input('Input number: '))

if n == 1 or n == 2:
    print('Number {} is  prime'.format(n))
elif n % 2 != 0:
    for i in range(2, n//2+1):
        if n % i == 0 and n != i:
            print('Number {} is not prime'.format(n))
            break
        if i == n//2:
            print('Number {} is  prime'.format(n))
else:
    print('Number {} is not prime'.format(n))
