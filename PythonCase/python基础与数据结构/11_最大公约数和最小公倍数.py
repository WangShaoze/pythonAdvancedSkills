def getMaxPublicNum(x: int, y: int):
    """
    最大公约数
        1.找到两个数字中小的那个
        2.从1开始遍历到小的那个数(包含)---如果能让两个数字多整除的数就放入列表，找到最后一个就是
    :param x:
    :param y:
    :return:
    """
    return [i for i in range(1, y if x > y else x + 1) if (x % i == 0) and (y % i == 0)][-1]


def getMinPublicNum(x: int, y: int):
    """
    找最小公倍数
        1.找到两个数字中大的那个
        2.从最大的那个数开始遍历找到一个能同时用x和y整除的数
    :param x:
    :param y:
    :return:
    """
    r = x if x > y else y
    while r:
        if (r % x == 0) and (r % y == 0):
            break
        r += 1
    return r


if __name__ == '__main__':
    print(getMaxPublicNum(12, 9))
    print(getMinPublicNum(102, 115))
