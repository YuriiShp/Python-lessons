# 1. У вас есть массив чисел. Напишите три функции, которые вычисляют
# сумму этих чисел: с for-циклом, с while-циклом, с *рекурсией.

def sum_w(arr):
    res = 0
    while arr:
        res += arr.pop(0)
    return res


def sum_f(arr):
    res = 0
    for el in arr:
        res += el
    return res


def sum_r(arr, summ=0):
    if arr:
        summ += arr.pop()
        return sum_r(arr, summ)
    else:
        return summ


def sum_r2(arr):
    if not arr:
        return 0
    else:
        res = arr.pop(0) + sum_r2(arr)
        return res


# 2. Напишите функцию, которая создаёт комбинацию двух списков таким
# образом: [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]

def mix(arr1, arr2):
    res = []
    for i in range(len(arr1)):
        res.extend([arr1[i], arr2[i]])
    return res


# 3. Существует ли треугольник с заданными сторонами.

def trexist(a, b, c):
    cond_1 = a + b > c
    cond_2 = a + c > b
    cond_3 = b + c > a

    if cond_1 and cond_2 and cond_3:
        return True
    else:
        return False


# 4. Расстояние между точками. На вход поступает два значение (кортежа) с
# координатами - широта и долгота.
# Найти расстояние между этими точками. cos(d) = sin(φА)·sin(φB) +
# cos(φА)·cos(φB)·cos(λА − λB), где φА и φB — широты, λА, λB — долготы
# данных пунктов, d — расстояние между пунктами, измеряется в
# радианах длиной дуги большого круга земного шара. Расстояние между
# пунктами, измеряемое в километрах, определяется по формуле: L = d·R,
# где R = 6371 км — средний радиус земного шара.

def map_dist(coord1, coord2):
    import math
    rz = 6371
    p1 = [el * math.pi / 180 for el in list(coord1)]
    p2 = [el * math.pi / 180 for el in list(coord2)]

    cosd = math.sin(p1[0]) * math.sin(p2[0]) + math.cos(p1[0]) * math.cos(p2[0]) * math.cos(p1[1] - p2[1])
    d = math.acos(cosd)
    l = d * rz
    return l


# 5. Поиск квадратных уравнений, имеющих решение. Программа принимает
# от пользователя диапазоны для коэффициентов a, b, c квадратного
# уравнения: ax2 + bx + c = 0. Перебирает все варианты целочисленных
# коэффициентов в указанных диапазонах, определяет квадратные уравнения,
# которые имеют решение.

def rootexist(ar, br, cr):
    res = []
    for a in range(ar[0], ar[1]+1):
        for b in range(br[0], br[1]+1):
            for c in range(cr[0], cr[1]+1):
                d = b**2 - 4 * a * c
                if d < 0:
                    tx = f'a = {a}; b = {b}; c = {c}  //  No Roots'
                elif d == 0:
                    tx = f'a = {a}; b = {b}; c = {c}  //  1 Root'
                else:
                    tx = f'a = {a}; b = {b}; c = {c}  //  2 Roots'
                print(tx)
                res.append(tx)
    return res


# 6. Заданы M строк символов, которые вводятся с клавиатуры. Каждая строка
# представляет собой последовательность символов, включающих в себя
# вопросительные знаки. Заменить в каждой строке все имеющиеся
# вопросительные знаки звёздочками.

def repsymb(*args):
    res = []
    for string in list(args):
        res.append(string.replace('?', '*'))
        print(string.replace('?', '*'))
    return res


# 7. Системная дата имеет вид 2009-06-15. Нужно преобразовать это значение
# в строку, строку разделить на компоненты (символ→разделитель→дефис),
# потом из этих компонентов сконструировать нужную строку. (2009-06-15 ->
# 15/06/2009)

def convdate(date):
    res_list = date.split('-')
    res_list.reverse()
    return '/'.join(res_list)


# 8. Задан вес в граммах. Определить вес в тоннах и килограммах.

def convmass(gr):
    return dict(m_kg=gr/10**3, m_ton=gr/10**6)


# 9. Имеется коробка со сторонами: A × B × C. Определить, пройдёт ли она в
# дверь с размерами M × K.

def fit(box, door):

    A = box[0] <= door[0] and box[1] <= door[1]
    B = box[0] <= door[1] and box[1] <= door[0]
    C = box[1] <= door[0] and box[2] <= door[1]
    D = box[1] <= door[1] and box[2] <= door[0]
    E = box[2] <= door[0] and box[0] <= door[1]
    F = box[2] <= door[1] and box[0] <= door[0]

    if A or B or C or D or E or F:
        return True
    else:
        return False


# 10. Можно ли из бревна, имеющего диаметр поперечного сечения D,
# выпилить квадратный брус шириной A?

def wood(d, sqr):
    if d**2 >= 2 * sqr**2:
        return True
    else:
        return False


# 11. Дан номер места в плацкартном вагоне. Определить, какое это место:
# верхнее или нижнее, в купе или боковое.

def choochoo(pl):
    if pl % 2 == 0:
        a = 'верхнє'
    else:
        a = 'нижнє'

    if pl > 36:
        b = 'бокове'
    else:
        b = 'купейне'

    return f'Місце {pl} - {a}, {b}'


# 12. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и
# монетой 2 грн., если это возможно.

def money(m):
    b500 = 0
    b100 = 0
    b10 = 0
    b2 = 0

    if m >= 500:
        b500 = m // 500
        m = m % 500
    if m >= 100:
        b100 = m // 100
        m = m % 100
    if m >= 10:
        b10 = m // 10
        m = m % 10
    b2 = m // 2
    m = m % 2

    res = {'500': b500, '100': b100, '10': b10, '2': b2}
    return res


# 13. Пользователь вводит число n, программа должна проверить является ли
# оно простым и сообщить об этом.

def isprime(num):
    cond = list()

    # перелічую умови за яких число не є простим, всього їх чотири. Якщо хоча б одна з них не
    # не виконується то число не є простим і функція повертає false
    cond.append(not (num % 2 == 0 and num != 2))     # not (число ділиться на 2 при цьому не дорівнює двом)
    cond.append(not (num % 3 == 0 and num != 3))     # not (число ділиться на 3 при цьому не дорівнює трьом)
    cond.append(not (num % 5 == 0 and num != 5))     # not (число ділиться на 5 при цьому не дорівнює пяти)
    cond.append(not (num % 7 == 0 and num != 7))     # not (число ділиться на 7 при цьому не дорівнює семи)

    for i in cond:
        if not i:
            return False
    return True


# 14. Вывести таблицу умножения числа M в диапазоне от числа a до числа b.
# # Числа M, a и b вводит пользователь.

def multtable(M, a, b):

    for n in range(a, b+1):
        print(f'{M} * {n} = {M*n}')
    return


# 15. Дан одномерный массив числовых значений, насчитывающий N
# элементов. Поменять местами элементы, стоящие на чётных и нечётных
# местах: A[1] ↔ A[2]; A[3] ↔ A[4] …

def mixer(arr):
    for i in range(0, len(arr), 2):
        if i != len(arr) - 1:
            arr.insert(i+1, arr.pop(i))
    return arr


# 16. Вывести список простых чисел в диапазоне d. Диапазон d вводит
# пользователь.

def selprime(arr):
    prime_list = list()
    for el in arr:
        if isprime(el):
            prime_list.append(el)
    return prime_list


