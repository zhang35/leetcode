class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Left -> Root -> Right
    def in_order(self, root) -> list:
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.data)
            res = res + self.in_order(root.right)
        return res

# Root -> Left ->Right
    def pre_order(self, root) -> list:
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res

# Left ->Right -> Root
    def post_order(self, root) -> list:
        res = []
        if root:
            res = self.post_order(root.left)
            res = res + self.post_order(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
print(root.in_order(root))
print(root.pre_order(root))
print(root.post_order(root))