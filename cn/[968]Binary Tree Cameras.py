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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)

# 官方题解…
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
         def dfs(root: TreeNode) -> List[int]:
             if not root:
                 return [float("inf"), 0, 0]
             la, lb, lc = dfs(root.left)
             ra, rb, rc = dfs(root.right)
             a = lc + rc + 1
             b = min(a, la + rb, ra + lb)
             c = min(a, lb + rb)
             return [a, b, c]
         a, b, c = dfs(root)
         return b
# leetcode submit region end(Prohibit modification and deletion)
