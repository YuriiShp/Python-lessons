arr_1 = list()


ar_len = int(input('Input array length: '))

for i in range(ar_len):
    num = int(input('Input number: '))
    if num % 2 == 0:
        continue
    arr_1.append(num)

print('Array: {}'.format(str(arr_1)))
