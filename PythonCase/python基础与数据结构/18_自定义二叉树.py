class Node:
    """
    节点类
    """

    def __init__(self, item):
        self.item = item
        self.child1 = None  # 左子节点
        self.child2 = None  # 右子节点


class BinaryTree:
    """
    二叉树类
    """

    def __init__(self):
        self.root = None  # 根节点
        self.result = []

    def add(self, item):
        """
        添加左右子节点元素
        :param item: 节点对应的元素
        :return:
        """
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)  # 每次抛出第0个数据后，第0个数据就会从列表移除
                if pop_node.child1 is None:
                    pop_node.child1 = node
                    return
                elif pop_node.child2 is None:
                    pop_node.child2 = node
                    return
                else:
                    q.append(pop_node.child1)
                    q.append(pop_node.child2)

    def preorder(self, root):
        """
        前序遍历
        :param root:
        :return: 前序遍历得到的结果
        """
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.child1)
        right_item = self.preorder(root.child2)
        return result + left_item + right_item

    def inorder(self, root):
        """
        中序遍历
        :param root:
        :return: 中序遍历 得到的结果
        """
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.child1)
        right_item = self.inorder(root.child2)
        return left_item + result + right_item

    def postorder(self, root):
        """
        后序遍历
        :param root:
        :return: 后序遍历得到的结果
        """
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.child1)
        right_item = self.postorder(root.child2)
        return left_item + right_item + result

    def everyLeval(self, root):
        """二叉树实现层次遍历"""
        pass


if __name__ == '__main__':
    t = BinaryTree()
    for i in "avoid":
        t.add(i)
    print("前序遍历：", t.preorder(t.root))
    print("中序遍历：", t.inorder(t.root))
    print("后序遍历：", t.postorder(t.root))

