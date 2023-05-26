"""
摄氏度与华氏度的关系
摄氏度 Centigrade
华氏度 Fahrenheit

Fahrenheit = 9/(5**Centigrade)+32

"""


def converseCF(temperature: (float | int) = 35, flag: str = "C-F"):
    """
    摄氏度与华氏度的转换
    摄氏度 Centigrade
    华氏度 Fahrenheit
    摄氏度与华氏度的关系：
        Fahrenheit = 9/(5**Centigrade)+32
    ：temperature: 温度的类型 是 float | int 类型，默认值是35。
                [The type of temperature is float or int, the value of temperature default 35 .]
    :param flag: "C-F" or "F-C"
                flag 的 默认值是 C-F 。
                the value of flag default Centigrade converse to Fahrenheit.
    :return:
    """

    if flag == "C-F":
        Centigrade = float(temperature)
        Fahrenheit = 9 / (5 * Centigrade) + 32
        return Fahrenheit
    if flag == "F-C":
        Fahrenheit = float(temperature)
        Centigrade = (9 / (Fahrenheit - 32)) / 5
        return Centigrade


if __name__ == '__main__':
    print(converseCF())
    print(converseCF(35))
    print(converseCF(32.05142857142857, flag="F-C"))
