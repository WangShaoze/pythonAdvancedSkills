class Stack:
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0

    def setSize(self, size):
        if size < self._current:  # 如果缩小了栈的空间，则删除已经有的元素
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def push(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current += 1
        else:
            print("Stack is full.")

    def pop(self):
        if self._content:
            self._current -= 1
            return self._content.pop()
        else:
            print("Stack is empty.")

    def show(self):
        print(self._content[-1])

    def empty(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self._current == self._size


if __name__ == '__main__':
    s = Stack()
    print("判断栈是否是空：", s.isEmpty())
    print("判断栈是否是已经满了：", s.isFull())

    s.push(1)
    s.push(2)
    s.push("a")
    print("显示栈顶的元素:")
    s.show()
    s.setSize(3)
    print("判断栈是否是已经满了：", s.isFull())
    print("栈的容量是:3 尝试向栈顶添加元素")
    s.push("b")
    print("弹出元素:{}".format(s.pop()))
    print("弹出元素:{}".format(s.pop()))
    print("弹出元素:{}".format(s.pop()))
    print("弹出元素:")
    s.pop()

