class Calculator:
    """
    实现一个简易计算器
    """
    @classmethod
    def addition(cls, *args, **kwargs):
        return sum(args) + sum([kwargs[k] for k in kwargs])

    @classmethod
    def subtraction(cls, m: int | float, n: int | float):
        return m - n

    @classmethod
    def division(cls, m: int | float, n: int | float):
        try:
            return m / n
        except Exception as e:
            print(e)
            print("除数不可以为0")
            return None

    @classmethod
    def multiplication(cls, *args, **kwargs):
        r = 1
        for i in args:
            r *= i
        for k in kwargs:
            r *= kwargs[k]
        return r


if __name__ == '__main__':
    print(Calculator.addition(12, 45, 89.2, 56))
    print(Calculator.addition(xio=12, li=15))
    print(Calculator.division(45, 46))
    print(Calculator.multiplication(12, 45, 13))
