#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (48.20%)
# Likes:    8909
# Dislikes: 246
# Total Accepted:    800.6K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,1,1,2,3]
# Output: [2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        p = dummy_head
        q = head

        while q:
            while q.next and q.val == q.next.val:
                q = q.next
            
            # q didn't moved
            if p.next == q:
                p = q
            # q moved. Duplication exists.
            else:
                p.next = q.next

            q = q.next

        return dummy_head.next

# @lc code=end

