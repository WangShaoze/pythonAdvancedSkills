def quickSort(li: list, low: int, high: int):
    # 判断low是否小于high,如果不小于直接返回原来的序列
    if low < high:
        i, j = low, high
        # 把小的那个数作为基准数
        base = li[i]
        while i < j:
            # 如果li后半区的数比 base 大或者相等，则前移动，直到有比 base 小的数出现
            while (i < j) and (li[j] >= base):
                j -= 1
                # 如果找到,
                li[i] = li[j]
                # 如果li前半区的数比 base 小或者相等，则后移动，直到有比 base 大的数出现
                while (i < j) and (li[i] <= base):
                    i += 1
                    li[j] = li[i]
        # 做完第一轮的循环之后，列表被分成两个半区，并且 此时 i=j
        li[i] = base
        # 将前后分区分别做递归
        # quickSort(li, low, i-1)
        # quickSort(li, j+1, high)
    return li


if __name__ == '__main__':
    s = [7, 2, 4, 1, 5, 8, 7, 6]
    print(quickSort(s, 0, len(s) - 1))
