# 给定一个二叉树，返回它的 后序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 450 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return None
        s1 = [root]
        s2 = []
        state = {} # none：not visited；1：right visited
        while s1:
            top = s1[-1]
            if not state.get(top):
                s2.append(top.val)
                if top.right: s1.append(top.right)
                state[top] = 1
            else:
                if top.left: s1[-1] = top.left
                else: s1.pop()
        s2.reverse()
        return s2
        
# leetcode submit region end(Prohibit modification and deletion)
