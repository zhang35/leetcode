#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (57.44%)
# Likes:    15453
# Dislikes: 391
# Total Accepted:    2.1M
# Total Submissions: 3.7M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,null,3,null,3]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def is_same(left, right):
#             if not left and not right:
#                 return True

#             if ((left == None) and (right != None)) or ((left != None) and (right == None)):
#                 return False
            
#             if left.val == right.val:
#                 return is_same(left.left, right.right) and is_same(left.right, right.left)
        
#         return is_same(root, root)

# Iterative
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root.left, root.right])

        while q:
            left = q.popleft()
            right = q.popleft()

            if not left and not right:
                continue

            if ((left == None) and (right != None)) or ((left != None) and (right == None)):
                return False
            
            if left.val != right.val:
                return False

            q.extend([left.left, right.right, left.right, right.left])

        return True
# @lc code=end

