# 给你一个二维整数数组 descriptions ，其中 descriptions[i] = [parenti, childi, isLefti] 表示 
# parenti 是 childi 在 二叉树 中的 父节点，二叉树中各节点的值 互不相同 。此外： 
# 
#  
#  如果 isLefti == 1 ，那么 childi 就是 parenti 的左子节点。 
#  如果 isLefti == 0 ，那么 childi 就是 parenti 的右子节点。 
#  
# 
#  请你根据 descriptions 的描述来构造二叉树并返回其 根节点 。 
# 
#  测试用例会保证可以构造出 有效 的二叉树。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# 输出：[50,20,80,15,17,19]
# 解释：根节点是值为 50 的节点，因为它没有父节点。
# 结果二叉树如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# 输出：[1,2,null,null,3,4]
# 解释：根节点是值为 1 的节点，因为它没有父节点。 
# 结果二叉树如上图所示。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= descriptions.length <= 10⁴ 
#  descriptions[i].length == 3 
#  1 <= parenti, childi <= 10⁵ 
#  0 <= isLefti <= 1 
#  descriptions 所描述的二叉树是一棵有效二叉树 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 数组 哈希表 二叉树 👍 16 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        vals = set()
        for x, y, left in descriptions:
            if left:
                nodes[x].left = nodes[y]
            else:
                nodes[x].right = nodes[y]
            vals.add(y)
        for v, node in nodes.items():
            node.val = v
        return next(node for v, node in nodes.items() if v not in vals)
# leetcode submit region end(Prohibit modification and deletion)
