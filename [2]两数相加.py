# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学 
#  👍 5040 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = ListNode(0, l1)
        h2 = ListNode(0, l2)
        carry = 0
        while h1.next and h2.next:
            tempSum = h1.next.val + h2.next.val + carry
            h1.next.val, carry = tempSum%10, tempSum//10
            h1 = h1.next
            h2 = h2.next
        if h2.next:
            h1.next = h2.next
        while h1.next:
            tempSum = h1.next.val + carry
            h1.next.val, carry = tempSum % 10, tempSum // 10
            h1 = h1.next
        if carry==1:
            h1.next = ListNode(1)
        return l1

# leetcode submit region end(Prohibit modification and deletion)
