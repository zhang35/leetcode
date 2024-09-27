#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (59.35%)
# Likes:    11795
# Dislikes: 361
# Total Accepted:    879.3K
# Total Submissions: 1.5M
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
# 
# 
# Example 1:
# 
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        left = head
        right = self.get_mid(head)
        # Cut the two parts
        right.next, right = None, right.next
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    

    def get_mid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

    def merge(self, list1, list2):
        head = tail = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return head.next
        
# @lc code=end

