# Given a binary tree 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#  
# 
#  Populate each next pointer to point to its next right node. If there is no ne
# xt right node, the next pointer should be set to NULL. 
# 
#  Initially, all next pointers are set to NULL. 
# 
#  
# 
#  Follow up: 
# 
#  
#  You may only use constant extra space. 
#  Recursive approach is fine, you may assume implicit stack space does not coun
# t as extra space for this problem. 
#  
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should popu
# late each next pointer to point to its next right node, just like in Figure B. T
# he serialized output is in level order as connected by the next pointers, with '
# #' signifying the end of each level.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given tree is less than 6000. 
#  -100 <= node.val <= 100 
#  
#  Related Topics 树 深度优先搜索 
#  👍 263 👎 0

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        leftmost = root # 第n层最左节点
        while leftmost:
            head = Node(0) # 第n+1层的虚拟头结点
            pre = head # 第n+1层的当前节点
            cur = leftmost # 第n层当前节点
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    pre.next = cur.right
                    pre = cur.right
                cur = cur.next
            leftmost = head.next # leftmost指向第n+1层最左节点
        return root
# leetcode submit region end(Prohibit modification and deletion)
