def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('На ноль делить нельзя!')
    return a / b


if __name__ == '__main__':
    print(add(3, 5))
    print(subtract(5, 3))
    print(multiply(3, 5))
    print(divide(15, 3))
