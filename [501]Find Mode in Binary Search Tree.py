# Given a binary search tree (BST) with duplicates, find all the mode(s) (the mo
# st frequently occurred element) in the given BST. 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than or equal t
# o the node's key. 
#  The right subtree of a node contains only nodes with keys greater than or equ
# al to the node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
# 
#  For example: 
# Given BST [1,null,2,2], 
# 
#  
#    1
#     \
#      2
#     /
#    2
#  
# 
#  
# 
#  return [2]. 
# 
#  Note: If a tree has more than one mode, you can return them in any order. 
# 
#  Follow up: Could you do that without using any extra space? (Assume that the 
# implicit stack space incurred due to recursion does not count). 
#  Related Topics 树 
#  👍 163 👎 0

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        cur = None
        count = 0
        maxCount = 0
        list = []
        def inorder(root):
            nonlocal cur, count, maxCount, list
            if root.left: inorder(root.left)
            if (root.val == cur):
                count += 1
            else:
                cur = root.val
                count = 1
            if count > maxCount:
                maxCount = count
                list = [cur]
            elif count == maxCount:
                list.append(cur)
            if root.right: inorder(root.right)

        if root: inorder(root)
        return list
# leetcode submit region end(Prohibit modification and deletion)

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
s = Solution()
print("res:", s.findMode(root))