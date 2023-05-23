def factorial(n):
    """
    计算阶乘
        (自然数)  0!=1, 4!=4x3x2x1
    :param n:
    :return:
    """
    r = 1
    if n != 0:
        for i in range(1, n + 1):
            r *= i
        return r
    if n == 0:
        return r
    if n < 0:
        return None


if __name__ == '__main__':
    print(factorial(4))
