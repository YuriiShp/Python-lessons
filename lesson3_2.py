arr = list()
even = 0

ar_len = int(input('Input array length: '))

for i in range(ar_len):
    num = int(input('Input number: '))
    if num % 2 != 0:
        even += 1
    arr.append(num)
odd = ar_len - even
print(arr)
print('Num of odd: {}'.format(odd))
print('Num of even: {}'.format(even))


