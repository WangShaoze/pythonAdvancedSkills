def isPrimerNum(n):
    """
    判断是否是质数
    0<=n<=2   是
    n>2   在 2～n 中，存在能整除n的数，n 不是质数
    n>2   在 2～n 中，不存在能整除n的数，n 是质数
    :param n:
    :return: True or False
    """
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    if n >= 0:
        return True
    return False


if __name__ == '__main__':
    for i in range(-10, 30):
        print("{} is 质数: {}".format(i, isPrimerNum(i)))

    # 计算 20～100 范围内的质数个数
    num = 0
    for i in range(20, 101):
        if isPrimerNum(i):
            num += 1
    print("20～100 范围内的质数个数：{}".format(num))
