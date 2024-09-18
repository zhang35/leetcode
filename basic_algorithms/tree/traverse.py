from collections import deque

class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

# Left -> Root -> Right
    def in_order(self, root) -> list:
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.val)
            res = res + self.in_order(root.right)
        return res

# Root -> Left ->Right
    def pre_order(self, root) -> list:
        res = []
        if root:
            res.append(root.val)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res

# Left ->Right -> Root
    def post_order(self, root) -> list:
        res = []
        if root:
            res = self.post_order(root.left)
            res = res + self.post_order(root.right)
            res.append(root.val)
        return res

    def bfs(self, root) -> list:
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def dfs(self, root) -> None:
        if root is None:
            return []

        print(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
    
    
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(15)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
print(root.in_order(root))
print(root.pre_order(root))
print(root.post_order(root))
print(root.bfs(root))

# For binary trees or general trees, DFS and pre-order traversal are equivalent.
root.dfs(root)