"""
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

0, 1
1, 1 + 0
1, 1 + 1
2, 2 + 1
3, 2 + 3


"""
from functools import lru_cache


@lru_cache(maxsize=None)
def solution(n: int):
    """
    >>> solution(4)
    3
    >>> solution(10)
    55
    >>> solution(36)
    ...
    """
    if n == 0:
        return 0
    last = 0
    next_ = 1
    for _ in range(1, n):
        last, next_ = next_, next_ + last
    return next_


"""
Рекурсия
f(x) = f(x - 2) + f(x - 1)
"""
"""
Мемонизированная рекурсия
"""
"""
lru_cache
"""
"""
Присвоение переменных
"""

if __name__ == '__main__':
    print(solution(4))