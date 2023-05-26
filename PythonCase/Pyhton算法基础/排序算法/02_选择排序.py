"""
选择排序
         # 找到最小值 min 的 index
n = 1  min ---> n < index = x1       li[n] = li[index]
n = 2  min ---> n < index = x2       li[n] = li[index]
n = 3  min ---> n < index = x2       li[n] = li[index]
...
"""


def selectOrder(li: list):
    for i in range(len(li)):
        for j in range(i, len(li)):
            if li[j] < li[i]:
                li[i], li[j] = li[j], li[i]


if __name__ == '__main__':
    s = [1, 78, 79, 56, 32, 41, 112, 45, 1, 4, 32]
    print(s)
    selectOrder(s)
    print(s)
