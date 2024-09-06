# Given a linked list, swap every two adjacent nodes and return its head. 
# 
#  You may not modify the values in the list's nodes. Only nodes itself may be c
# hanged. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 100]. 
#  0 <= Node.val <= 100 
#  
#  Related Topics 链表 
#  👍 680 👎 0

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head

        pre = head
        post = pre.next
        head = post
        # 虚节点
        lastTail = ListNode(0)
        lastTail.next = pre
        while True:
            pre.next = post.next
            post.next = pre
            lastTail.next = post
            lastTail = pre

            pre = pre.next
            if not pre: break
            post = pre.next
            if not post: break
        return head
# leetcode submit region end(Prohibit modification and deletion)
