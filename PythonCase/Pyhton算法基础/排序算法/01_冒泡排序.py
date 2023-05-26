"""
冒泡排序
    (1) 从前往后遍历到n-1，判断相邻两个数，如果前者比后者大，这交换两个数的位置。
    (2) 第一条执行n-1次即可
"""


def popOrder(li: list):
    for j in range(len(li) - 1):
        for i in range(len(li) - 1):
            if li[i + 1] < li[i]:
                li[i + 1], li[i] = li[i], li[i + 1]


if __name__ == '__main__':
    s = [1, 78, 79, 56, 32, 41, 112, 45, 1, 4, 32]
    print(s)
    popOrder(s)
    print(s)
