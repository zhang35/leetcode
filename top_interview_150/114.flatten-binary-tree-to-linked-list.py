#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (66.22%)
# Likes:    12404
# Dislikes: 566
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given the root of a binary tree, flatten the tree into a "linked list":
# 
# 
# The "linked list" should use the same TreeNode class where the right child
# pointer points to the next node in the list and the left child pointer is
# always null.
# The "linked list" should be in the same order as a pre-order traversal of the
# binary tree.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right    # We go to left Subtree's rightMost Node
                prev.right = cur.right   #We make current Node's right Subtree prev's right Subtree
                cur.right = cur.left    # We make it right Subtree
                cur.left = None   # Removing left 
            
            cur = cur.right	

 					# 	  1
					#    / \
					#   2   5
					#  / \   \
					# 3   4   6
					
                    # 	 1
					#    / 
					#   2   
					#  / \   
					# 3   4   
					# 	   \
					# 		 5
					# 		   \
					# 		     6

					# 	1
					# 	  \
					# 		2   
					# 	   /  \   
					# 	  3    4   
					# 	     	   \
					# 				 5
					# 				   \
					# 					 6
					   
					# 	1
					# 	  \
					# 		2   
					# 	   /     
					# 	  3    
					#         \
					# 		  4   
					# 		    \
					# 			  5
					# 			    \
					# 				  6
							
					# 	1
					# 	  \
					# 		2
					# 		  \
					# 		    3    
					# 			   \
					# 				  4   
					# 					\
					# 					  5
					# 						\
					# 						  6
							  
							  
						  	
# @lc code=end

