A = {
    "employer_01": 1000,
    "employer_02": 2000,
    "employer_03": 500,
    "employer_04": 4000
}

B = {
    "employer_05": 10000,
    "employer_06": 2000,
    "employer_03": 5000,
    "employer_04": 2000
}


def solution_1():
    """
    Мы хотим получить самого высокого оплачиваемого работника из двух отделов, по одной ставке
    >>> solution_1()
    employer_05
    """
    max_ = -1
    set_A = set(A.keys())
    set_B = set(B.keys())
    two = set_A.intersection(set_B)
    for d in zip([A, B]):
        max_ = ([max_, *map(lambda x: d[x], set(d.keys()).difference(two))])

    ...

"""
intersection
"""


def solution_2():
    """
    Мы хотим получить самого высокого оплачиваемого работника из отдела А,
    зарплата берется суммой из двух отделов
    >>> solution_2()
    employer_04
    """
    ...

"""
intersection
"""


def solution_3():
    """
    Мы хотим получить самого высокого оплачиваемого работника из отдела А,
    только для тех кто работает в этом отделе
    >>> solution_2()
    employer_02
    """
    ...

"""
difference
"""


"""
set.issubset(other)   все элементы set принадлежат other.
set.issuperset(other) все элементы other принадлежат set.
set.union(other, ...) объединение нескольких множеств.
"""