arr_1 = list()
arr_2 = list()


ar_len = int(input('Input array length: '))

for i in range(ar_len):
    num = int(input('Input number: '))
    arr_1.append(num)
    num += 1
    arr_2.append(num)
print('First Array: {}'.format(str(arr_1)))
print('Second Array: {}'.format(str(arr_2)))
