def solution(items):
    """
    map(int, input.split())
    Получить массив сумм двух чисел через 1
    >>> solution([1, 2, 3, 4, 7, 2, 1, 1])
    [5, 9]
    """
    return list(map(sum, zip(items[1::3], items[2::3])))


"""
slice, zip, map, list
"""