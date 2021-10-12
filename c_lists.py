def solution(items):
    """
    [1, 2, 3, 4, 5, 6, 7]
    [[1, 2, 3], 4, 5, 6, 7]
    [1, [2, 3, 4], 5, 6, 7]
    [1, 2, [3, 4, 5], 6, 7]
    Вывести числа, которые являтся суммой двух предыдущих или двух последующих
    >>> solution([1, 2, 3, 4, 7, 2, 1, 1])
    [3, 2, 7]
    """
    result = []
    left = 2
    right = len(items) - 3
    while left < len(items) - 1:
        if items[left] == (items[left - 1] + items[left - 2]):
            result.append(items[left])
        if items[right] == (items[right + 1] + items[right + 2]):
            result.append(items[right])
        left += 1
        right -= 1
    return result


"""
Проходим в обе стороны
"""
