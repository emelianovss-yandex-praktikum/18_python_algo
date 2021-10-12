def solution(string, sub_string):
    """
    Надо найти подстроку в строке в любой последовательности
    False
    """
    for s in sub_string:
        string = string.replace(s, "%")
    print(string)
    return "%" * len(sub_string) in string


"""
product
"""
"""
Проверка вхождения, remove
"""
"""
replace
"""


if __name__ == '__main__':
    print(solution("hello world", "wor"))
    print(solution("hello world", "orw"))
    print(solution("hello world", "war"))
