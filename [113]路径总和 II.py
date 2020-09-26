# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#  Related Topics 树 深度优先搜索 
#  👍 329 👎 0

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        list = []
        path = []
        def dfs(node, curSum):
            if not node: return
            curSum += node.val
            path.append(node.val)
            if not node.left and not node.right and curSum==sum:  #leave node
                list.append(path[:])  #复制出整个序列,否则是传引用，后面修改path会影响list里的值
            if node.left: dfs(node.left, curSum)
            if node.right: dfs(node.right, curSum)
            path.pop() #注意恢复path
        dfs(root, 0)
        return list
# leetcode submit region end(Prohibit modification and deletion)
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
s = Solution()
list = s.pathSum(root, 22)
print(list)
