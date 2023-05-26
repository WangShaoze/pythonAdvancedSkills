"""
二次方程求解
a*x**2+b*x+c = 0
利用求根公式求解
d=(b**2)-(4*a*c)
s1 = (-b-math.sqrt(d))/(2*a)
s2 = (-b+math.sqrt(d))/(2*a)
"""
import math
import re


def getResult(equation: str = "x^2+2x-3=0"):
    """
    一元二次方程求解
     方法:
        二次方程求解
        a*x**2+b*x+c = 0
        利用求根公式求解
        d=(b**2)-(4*a*c)
        s1 = (-b-math.sqrt(d))/(2*a)
        s2 = (-b+math.sqrt(d))/(2*a)
    :param equation: 一元二次方程式
    :return: (s1,s2) 或 无解
    """
    prog = re.compile("(?P<a>.*?)x\^2(?P<b>.*?)?x?(?P<c>.*?)?=0", re.S)
    data = prog.match(equation)
    a = data.group("a")
    b = data.group("b")
    c = data.group("c")
    if a == "":
        a = 1
    if a == "-":
        a = -1
    if b == "":
        if "x" in c:
            # 解析c
            b = c.split("x")[0]
            c = c.split("x")[1]
            if c == "":
                c = 0
        else:
            b = 0
            c = 0
    a, b, c = float(a), float(b), float(c)
    try:
        d = (b ** 2) - (4 * a * c)
        s1 = (-b - math.sqrt(d)) / (2 * a)
        s2 = (-b + math.sqrt(d)) / (2 * a)
        return s1, s2
    except Exception as e:
        print(e)
        return "无解"


print(getResult())
