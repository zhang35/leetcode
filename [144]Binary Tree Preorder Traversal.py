# Given the root of a binary tree, return the preorder traversal of its nodes' v
# alues. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,2]
# Output: [1,2]
#  
# 
#  Example 5: 
# 
#  
# Input: root = [1,null,2]
# Output: [1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  Follow up: 
# 
#  Recursive solution is trivial, could you do it iteratively? 
# 
#  
#  Related Topics 栈 树 
#  👍 415 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        def dfs(cur):
            if not cur: return
            ret.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
