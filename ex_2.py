def fun_sum(arr):
    summ = 0
    for i in arr:
        summ += i
    return summ


def fun_sum_2(arr):
    summ = 0
    while arr:
        summ += arr.pop()
    return summ


def fun_sum_r(arr, summ=0):
    if arr:
        summ += arr.pop()
        return fun_sum_r(arr, summ)
    else:
        return summ


######################################################################
def fun_mix(list1, list2):
    r = []
    for i in range(len(list1)):
        r.extend([list1[i], list2[i]])
    return r


def fun_replace(str_list, smb1, smb2):
    new_list = []
    for i in str_list:
        new_list.append(i.replace(smb1, smb2))
    return new_list


def fun_date(d):
    ls = list(d.split('-'))
    ls.reverse()
    return '/'.join(ls)


def fun_mass(gr):
    m_kg = round(gr / 10**3, 3)
    m_ton = round(gr / 10**6, 3)
    return m_kg, m_ton


dict_4_func = {'arg1': 10, 'arg2': 31, 'arg3': 'X'}


def func_dict(arg1, arg2, *args, **kwargs):
    return arg1 + arg2


print(func_dict(**dict_4_func))

#######################################################################

# decorator


def decorator_line(fun_to_decorate):
    def wrapper():
        print('------------')
        fun_to_decorate()
        print('------------')
    return wrapper


def decorator_plus(fun_to_decorate):
    def wrapper():
        print('+++++++++++++')
        fun_to_decorate()
        print('+++++++++++++')
    return wrapper


@decorator_line
@decorator_plus
def print_name():
    print('Hello')

