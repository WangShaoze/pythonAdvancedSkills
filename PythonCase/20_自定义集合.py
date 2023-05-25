class Student:
    def __init__(self, name, score):  # 初始化各个形式参数
        self.name = name
        self.score = score

    def __hash__(self):
        """
        使用__hash__哈希算法，把形式参数转化为一个数值，再用__eq__把转换过来的数值进行比较
        :return:
        """
        return self.name.__hash__()

    def __eq__(self, other):
        if self.score == other.score:  # 把转换过来的数值进行比较
            return True
        return False

    def __repr__(self):
        """
        ；自定义类实现自我描述的功能
        :return:
        """
        return self.name + "：{}".format(self.score)


if __name__ == '__main__':
    # 自定义集合
    u1 = Student("xioWang", 12)
    u2 = Student("xioHua", 10)
    u3 = Student("xioZhang", 13)
    u4 = Student("xioLan", 15)
    u5 = Student("xioHu", 11)
    u6 = Student("xioJi", 15)

    a = {u1, u2, u3, u4}
    b = {u2, u4, u5, u6}

    # 创建u和s两个集合
    u = set(a)
    s = set(b)
    print("原来的集合 u 为:{}".format(u))
    print("原来的集合 s 为:{}".format(s))

    # 进行增加删除操作
    u.remove(u2)
    print("删除后的集合 u 为:{}".format(u))
    print("删除后的集合 s 为:{}".format(s))

    # 集合的运算并输出
    print("集合 u 与 集合 s 的 并集:{}".format(u | s))
    print("集合 u 与 集合 s 的 交集:{}".format(u & s))
    print("集合 u 与 集合 s 的 差集:{}".format(u - s))
    print("集合 s 与 集合 u 的 差集:{}".format(s - u))
