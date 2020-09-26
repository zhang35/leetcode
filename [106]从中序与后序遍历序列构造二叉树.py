# Given a binary tree, we install cameras on the nodes of the tree. 
# 
#  Each camera at a node can monitor its parent, itself, and its immediate child
# ren. 
# 
#  Calculate the minimum number of cameras needed to monitor all nodes of the tr
# ee. 
# 
#  
# 
#  Example 1: 
# 
#  
#  
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree.
#  The above image shows one of the valid configurations of camera placement.
#  
# 
#  
# Note: 
# 
#  
#  The number of nodes in the given tree will be in the range [1, 1000]. 
#  Every node has value 0. 
#  
#  
#  
#  Related Topics 树 深度优先搜索 动态规划 
#  👍 171 👎 0

from typing import List
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def fun(root, l, r, inorder, postorder):
            if l > r : return
            node = TreeNode(postorder[root])
            k = l
            while k<r and inorder[k]!=postorder[root]: k = k+1
            node.left = fun(root-1-r+k, l, k-1, inorder, postorder)
            node.right = fun(root-1, k+1, r, inorder, postorder)
            return node
        n = len(postorder)
        return fun(n-1, 0, n-1, inorder, postorder)

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
node = s.buildTree(inorder, postorder)
q = Queue()
q.put(node)
while not q.empty():
    node = q.get()
    print(node.val)
    if node.left: q.put(node.left)
    if node.right: q.put(node.right)
