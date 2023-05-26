import copy


class Matrix:
    def __init__(self, row, column, fill=0.0):
        """
        初始化矩阵
        :param row: 矩阵的行数
        :param column: 矩阵的列数
        :param fill: 矩阵的初始值
        """
        self.shape = (row, column)  # 矩阵的维度
        self.row = row
        self.column = column
        self._matrix = [[fill] * column for i in range(row)]  # 生成初始矩阵

    def __getitem__(self, index):
        """
        获取矩阵的值，
        :param index: int------> row, tuple-------> (row, column)
        :return:
        """
        if isinstance(index, int):
            return self._matrix[index - 1]
        elif isinstance(index, tuple):
            return self._matrix[index[0] - 1][index[1] - 1]

    def __setitem__(self, index, value):
        """
        给矩阵设置值
        :param index: 位置 int------> row--------> [,,,] , tuple-------> (row, column)-----> 元素
        :param value: 需要设置的值
        :return:
        """
        if isinstance(index, int):
            self._matrix[index - 1] = copy.deepcopy(value)  # 对用户输入的列表进行深拷贝
        elif isinstance(index, tuple):
            self._matrix[index[0] - 1][index[1] - 1] = value

    def __eq__(self, other):
        """
        比较矩阵的维度
        :param other: 需要比较的实例
        :return: bool 类型
        """
        assert isinstance(other, Matrix), "类型不匹配，不能比较"
        return other.shape == self.shape  # 在类型匹配的前提下，比较维度，即行列

    def __add__(self, other):
        """加法"""
        assert other.shape == self.shape, "维度不匹配，不能相加"
        M = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                M[r, c] = self[r, c] + other[r, c]
        return M

    def show(self):
        """
        展示矩阵
        :return:
        """
        for r in range(self.row):
            for c in range(self.column):
                print(self[r + 1, c + 1], end="   ")
            print()


if __name__ == '__main__':
    m = Matrix(3, 3, fill=0.0)
    n = Matrix(3, 3, fill=0.0)
    m[1] = [1., 2., 3.]
    m[2] = [4., 5., 6.]
    n[1] = [6., 8., 6.]
    n[2] = [1., 0., 3.]
    n[3] = [4., 9., 2.]
    p = m + n
    print("n = ")
    n.show()
    print()
    print("m = ")
    m.show()
    print()
    print("p = ")
    p.show()
    print()
    print("p[1,1]", p[1, 1])
