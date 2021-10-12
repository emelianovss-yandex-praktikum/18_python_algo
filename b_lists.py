def solution(items):
    """
    Надо заменить все элементы "с" на четных позициях, на "d"
    >>> solution(["a", "b", "c", "c", "a", "c"])
    ['a', 'b', 'c', 'd', 'a', 'd']
    """
    index = -1
    while index < len(items):
        try:
            index = items.index("c", index + 1)
            items[index] = "d"
        except ValueError:
            pass
    return items


"""
list.index
"""
"""
enumerate
"""
"""
zip,map,range
"""
