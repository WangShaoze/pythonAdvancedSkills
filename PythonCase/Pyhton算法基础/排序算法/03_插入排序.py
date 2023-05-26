"""
简单插入排序
"""


def insertOrder(li: list):
    for i in range(1, len(li)):
        # 判断相邻两个元素的大小
        j = i - 1
        if li[j] > li[i]:
            temp = li[i]  # 将 较小的那个数 存储到临时 temp ，并将其位置上的数替换为 较的的那个数
            li[i] = li[j]

            # 寻找 较小的那个数 的插入位置
            j -= 1
            while j >= 0 and li[j] > temp:   # 向前找数，如果该数大于temp就往后移动一位，当找到小于或者等于的时候，退出
                li[j + 1] = li[j]
                j -= 1
            li[j + 1] = temp


if __name__ == '__main__':
    s = [7, 6, 5, 4, 3, 2, 1, 0]
    print(s)
    insertOrder(s)
    print(s)
