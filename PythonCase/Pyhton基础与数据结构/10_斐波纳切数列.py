def getFibLi(n: int):
    """
    斐波纳切数列 ： 基数 0和1 ，后面每一项 是 前面两项之和
    :param n:  数列长度 必须大于0
    :return: 数列
    """
    if n == 1:
        return [0, ]
    if n == 2:
        return [0, 1]
    li = [0, 1]
    for i in range(2, n):
        li.append(li[-2] + li[-1])
    return li


if __name__ == '__main__':
    print(getFibLi(1))
    print(getFibLi(2))
    print(getFibLi(4))
