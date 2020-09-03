# def power(num, p1, p2):
#     res_dict = dict()
#     for i in range(p1, p2+1):
#         res_dict.update({f'{num}^{i}:': i})
#     return res_dict
#
#
# res_d = power(2, 2, 5)
# print(res_d)
#
#
# # VAR 2
# def power(num, p1, p2):
#     res_dict = [{f'{num}^{el}': num**el} for el in range(p1, p2+1)]
#     return res_dict
#
#
# res_d = power(2, 2, 5)
# print(res_d)

# # ex 1
# def digitsum(num):
#     str_num = str(num)
#     summ = 0
#     for i in str_num:
#         summ += int(i)
#     return summ
#
#
# res = digitsum(1256)
# print(res)

# # ex 2
# def numreverse(num):
#     list_digits = list(str(num))
#     list_digits.reverse()
#     str_digits = ''.join(list_digits)
#     res = int(str_digits)
#     return res


# res = numreverse(1256)
# print(res)

# # ex 3
# def fib(n_iter):
#     start = [1, 1]
#     for i in range(n_iter):
#         new_el = start[-1] + start[-2]
#         start.append(new_el)
#     return start
#
#
# res = fib(3)
# print(res)

#
# # ex 3v2
# def fib(rng):
#     start = [1, 1]
#     while True:
#         new_el = start[-1] + start[-2]
#         if new_el >= rng:
#             break
#         start.append(new_el)
#     return start
#
#
# res = fib(56)
# print(res)

# # ex 4
# def prodsum(num):
#     str_num = str(num)
#     summ = 0
#     prod = 1
#     for i in str_num:
#         summ += int(i)
#         prod *= int(i)
#     return summ, prod
#
#
# res_sum, res_prod = prodsum(1256)
# print(f'{res_sum}\n{res_prod}')

# # ex 5
# def bubble(n_list):
#     for i in range(len(n_list)):
#         if i+1 != len(n_list):
#             if n_list[i] > n_list[i+1]:
#                 n_list.insert(i+1, n_list.pop(i))
#                 bubble(n_list)
#     return n_list
#
#
# some_list = [1, 6, 3, 7, 8, 0, 2, 5, 1, 1, 9]
# print(bubble(some_list))
#
# def bubble2(n_list):
#     for i in range(len(n_list)-1):
#         for j in range(len(n_list)-i-1):
#             if n_list[j] > n_list[j+1]:
#                 n_list[j], n_list[j+1] = n_list[j+1], n_list[j]
#                 print(n_list)
#     return n_list
#
#
# some_list = [1, 6, 3, 7, 8, 0, 2, 5, 1, 1, 9]
# print(bubble2(some_list))


# # ex 6
# def unique(text):
#     # buff_str = ''
#     # for ch in text:
#     #     if ch in buff_str:
#     #         return False
#     #     buff_str += ch
#     # return True
#     if len(set(text)) == len(text):
#         return True
#     else:
#         return False
#
#
# text1 = 'cat'
# text2 = 'cat rat'
#
# print(unique(text1))
# print(unique(text2))

