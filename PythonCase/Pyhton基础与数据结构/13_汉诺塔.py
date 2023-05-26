s = 0


def move(n, a, b, c):
    """
    汉诺塔
        法国数学家爱德华·卢卡斯曾编写过一个印度的古老传说：在世界中心贝拿勒斯（在印度北部）的圣庙里，
        一块黄铜板上插着三根宝石针。印度教的主神梵天在创造世界的时候，在其中一根针上从下到上地穿好了由大到小的64片金片，
        这就是所谓的汉诺塔。不论白天黑夜，总有一个僧侣在按照下面的法则移动这些金片：
        一次只移动一片，不管在哪根针上，小片必须在大片上面。僧侣们预言，当所有的金片都从梵天穿好的那根针上移到另外一根针上时，
        世界就将在一声霹雳中消灭，而梵塔、庙宇和众生也都将同归于尽。
    :param n: 片的个数
    :param a: 桩1
    :param b: 桩2
    :param c: 桩3
    :return: 移动次数
    """
    global s
    if n == 1:
        s += 1
        print("第{}块：从{}柱---->{}柱  {}次".format(n, a, c, s))
    else:
        # n = 2    1: a--->b    2: a---->c    1: b---->c
        # n = 3    1: a--->b    2: a---->c    1: b---->c
        #          3: a--->b    1: c---->b    2: c---->a
        #          1: b--->a    3: b---->c    1: a---->b   2: a---->c  1: a--->c
        move(n - 1, a, c, b)  # n-1 第一次移动
        s += 1
        print("第{}块：从{}柱---->{}柱  {}次".format(n, a, c, s))
        move(n - 1, b, a, c)  # n-1 第二次移动


move(15, "A", "B", "C")


def f(n):
    if n == 0:
        return 0
    else:
        return 2 * f(n - 1) + 1


x = int(input("请输入片的个数："))
print("需要移动", f(x), "次")

