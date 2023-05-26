class MyQueue:
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0

    def setSize(self, size):
        """
        设置队列的大小
        :param size:   队列大小
        :return:
        """
        if size < self._current:  # 如果缩小队列，需要删除后面的元素
            for i in range(size, self._current)[::-1]:  # 从队尾开始删除
                del self._content[i]
            self._current = size
        self._size = size

    def put(self, v):  # 实现入队
        """入队"""
        if self._current < self._size:
            self._content.append(v)
            self._current += 1
        else:
            print("The queue is full.")

    def get(self):  # 实现出队
        """出队"""
        if self._content:
            self._current -= 1
            return self._content.pop(0)
        else:
            print("The queue is empty.")

    def show(self):
        """显示队列"""
        if self._content:
            print(self._content)
        else:
            print("The queue is empty.")

    def empty(self):
        """清空队列"""
        self._content = []

    def isEmpty(self):
        """判断是否已经是空队列了"""
        if not self._content:
            return True
        else:
            return False

    def isFull(self):
        """判断是否已经是满队列了"""
        if self._current == self._size:
            return True
        else:
            return False


if __name__ == '__main__':
    q = MyQueue()
    print("队列元素出队：")
    q.get()
    print("队列元素入队：")
    q.put(12)
    q.put(46)
    q.put(3)
    q.put(5)
    q.put(4)
    q.put(6)
    print("队列的元素:")
    q.show()
    print("队列是否已满:{}".format(q.isFull()))
    q.setSize(2)
    print("队列的元素:")
    q.show()
    print("队列是否已满:{}".format(q.isFull()))
    print("尝试添加元素:")
    q.put(3)
