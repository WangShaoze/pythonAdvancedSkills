def isArmsNum(n: int):
    """
    阿姆斯特朗数  153 = 1^3+5^3+3^3
    :param n:
    :return:
    """
    r = 0
    for i in range(len(str(n))):
        r += int(str(n)[i]) ** (len(str(n)))
    if r == n:
        return True
    return False


if __name__ == '__main__':
    print(isArmsNum(153))
    print(isArmsNum(121))

    asl = []
    for num in range(1, 10000):
        if isArmsNum(num):
            asl.append(num)

    print(asl)
    print(len(asl))
