# Given head, the head of a linked list, determine if the linked list has a cycl
# e in it. 
# 
#  There is a cycle in a linked list if there is some node in the list that can 
# be reached again by continuously following the next pointer. Internally, pos is 
# used to denote the index of the node that tail's next pointer is connected to. N
# ote that pos is not passed as a parameter. 
# 
#  Return true if there is a cycle in the linked list. Otherwise, return false. 
# 
# 
#  Follow up: 
# 
#  Can you solve it using O(1) (i.e. constant) memory? 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to t
# he 1st node (0-indexed).
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to t
# he 0th node.
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the list is in the range [0, 104]. 
#  -105 <= Node.val <= 105 
#  pos is -1 or a valid index in the linked-list. 
#  
#  Related Topics 链表 双指针 
#  👍 808 👎 0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = p2 = head
        while True:
            if p1: p1 = p1.next
            if p2: p2 = p2.next
            if p2: p2 = p2.next
            else: return False
            if p1==p2: return True
# leetcode submit region end(Prohibit modification and deletion)
