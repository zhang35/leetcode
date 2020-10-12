# Given a binary search tree with non-negative values, find the minimum absolute
#  difference between values of any two nodes. 
# 
#  Example: 
# 
#  
# Input:
# 
#    1
#     \
#      3
#     /
#    2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 
# (or between 2 and 3).
#  
# 
#  
# 
#  Note: 
# 
#  
#  There are at least two nodes in this BST. 
#  This question is the same as 783: https://leetcode.com/problems/minimum-dista
# nce-between-bst-nodes/ 
#  
#  Related Topics 树 
#  👍 169 👎 0

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minDist = 0x3f3f3f3f
        if not root: return minDist
        if root.left:
            l = root.left
            while l.right: l = l.right
            dist = root.val-l.val
            if dist < minDist: minDist = dist
        if root.right:
            r = root.right
            while r.left: r = r.left
            dist = r.val - root.val
            if dist < minDist: minDist = dist
        minDist = min(self.getMinimumDifference(root.left), self.getMinimumDifference(root.right), minDist)
        return minDist
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
root = TreeNode(10)
root.left = TreeNode(1)
root.right = TreeNode(17)
root.right.left = TreeNode(15)
print(s.getMinimumDifference(root))