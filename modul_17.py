def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

while True:
    try:
        array = input("Введите целые числа через пробел: ")
        L = list(map(int, array.split()))  # преобразовываем последовательность в список
    except ValueError:
        print("Error! Данные введены некорректно, попробуйте ещё раз.")
    else:
        L_sort = merge_sort(L) # выполняем сортировку
        print("Отсортированный список: ", L_sort)
        break

while True:
    try:
        element = int(input("Введите целое число из диапазона последовательности чисел: "))
    except ValueError:
        print("Error! Данные введены некорректно.")
    else:
        if element > L_sort[0] and element < L_sort[-1]:
            L_sort.append(element)  # добавляем введённое число в конец списка
            L_sort_addel = merge_sort(L_sort)  # опять выполняем сортировку
            index = binary_search(L_sort_addel, element, 0, len(L_sort_addel)-1) # индекс введённого числа
            #print(L_sort_addel)
            if L_sort_addel[index] > L_sort_addel[index-1]:
                print("Номер индекса элемента, который меньше введённого числа: ", index-1)
            else:
                print("Номер индекса элемента, который меньше введённого числа: ", index-2)
        else:
            print("Данное число не из диапазона")
        break