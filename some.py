def sum_(a, b):
    stack = [1 for _ in range(b)]
    while stack:
        a += stack.pop()
    return a


if __name__ == '__main__':
    print(sum_(10, 5))