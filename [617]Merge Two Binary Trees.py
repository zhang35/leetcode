# Given two binary trees and imagine that when you put one of them to cover the 
# other, some nodes of the two trees are overlapped while the others are not. 
# 
#  You need to merge them into a new binary tree. The merge rule is that if two 
# nodes overlap, then sum node values up as the new value of the merged node. Othe
# rwise, the NOT null node will be used as the node of new tree. 
# 
#  Example 1: 
# 
#  
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
#  
# 
#  
# 
#  Note: The merging process must start from the root nodes of both trees. 
#  Related Topics 树 
#  👍 486 👎 0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if (not t1): return t2
        if (not t2): return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# leetcode submit region end(Prohibit modification and deletion)
# test case
t1 = TreeNode(1)
t2 = TreeNode(2)
t1.left = TreeNode(3)
t2.right = TreeNode(4)
t2.right.left = TreeNode(5)
t2.right.right = TreeNode(6)
s = Solution()
t = s.mergeTrees(t1, t2)
print(t.val, t.left.val, t.right.val)
