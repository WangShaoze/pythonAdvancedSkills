"""
平年
闰年 判断规则如下:

年份 不可以整除4为平年
     可以整除100 但不可以整除 400为平年
     其余为闰年

"""


def leapYear(year: int):
    """
    判断是否是闰年
        年份 不可以整除4为平年
        可以整除100 但不可以整除 400为平年
        其余为闰年

    :param year:  闰年 平年
    :return:      True False
    """
    if year % 4 != 0:
        return False
    if (year % 100 == 0) and (year % 400 != 0):
        return False
    return True


print(leapYear(2100))

