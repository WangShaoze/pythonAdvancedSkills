class MyArray:
    @staticmethod
    def __isNumber(n):
        if not isinstance(n, (int, float, complex)):
            return False
        return True

    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__isNumber(arg):
                    print('All elements must be numbers!!')
                    return
            self.__value = list(args)

    def __add__(self, other):
        if self.__isNumber(other):
            b = MyArray()
            b.__value = [item + other for item in self.__value]
            return b
        elif isinstance(other, MyArray):
            if len(other.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i + j for i, j in zip(self.__value, other.__value)]
                return c
            else:
                print('Length of other Array is not equal to self Array.')
        else:
            print('Not supported.')

    def dot(self, v):
        if not isinstance(v, MyArray):
            print("The v must be an instance of MyArray.")
            return
        if len(v) != len(self.__value):
            print("Length of v must be equal to self.")
            return
        return sum([i * j for i, j in zip(self.__value, v.__value)])

    def __len__(self):
        return len(self.__value)

    def __str__(self):
        return str(self.__value)

    def __contains__(self, n):
        """
        __contains__()方法
        python 内置方法__contains__()，可以用于判断参数指定的值value是否为调用对象中的元素。
        如果是，则返回True，否则返回False，与成员运算符in的功能相当。
        提示：调用对象可以是python的可迭代对象，如list、tuple、dict、set、str等等。
        :param n:
        :return:
        """
        if n in self.__value:
            return True
        return False

    def append(self, n):
        if isinstance(n, (float, int)):
            self.__value.append(n)
        else:
            print("isinstance error")

    def __repr__(self):
        """
        __repr__() 是 Python 类中的一个特殊方法，由 object 对象提供，由于所有类都是 object 类的子类，所以所有类都会继承该方法。
        该方法主要实现 “自我描述” 功能——当直接打印类的实例化对象时，系统将会自动调用该方法，
        输出对象的自我描述信息，用来告诉外界对象具有的状态信息。
        :return:
        """
        return repr(self.__value)  # repr() 函数将对象转化为供解释器读取的形式，repr()
        # 方法可以将读取到的格式字符，比如换行符、制表符，转化为其相应的转义字符

    def __getitem__(self, key):
        length = len(self.__value)
        if isinstance(key, int) and 0 <= key < length:
            return self.__value[key]
        else:
            return "Index Error"

    def __setitem__(self, key, value):
        length = len(self.__value)
        if isinstance(key, int) and 0 <= key < length:
            self.__value[key] = value
        else:
            return "Index Error"


if __name__ == "__main__":
    a = MyArray(1, 2, 3, 4, 5, 6)
    b = MyArray(6, 5, 4, 3, 2, 1)
    print("数组a:", a)
    print("数组b:", b)
    print("a+b", a + b)
    print("a,b数组内积：", a.dot(b))
    print("2在数组a内？", 2 in a)
    a.append(45)  # 向a数组添加45这个元素
    print("向a数组添加45这个元素：{}".format(a))
    print("查看数组a的第三个元素：{}".format(a[2]))
    a[5] = 2323  # 修改第6个元素
    print("修改第6个元素:{}".format(a))
