#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (51.07%)
# Likes:    15107
# Dislikes: 1344
# Total Accepted:    1.6M
# Total Submissions: 3.1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        total = m * n
        res = []

        while total > 0:
            for i in range(left, right+1):
                res.append(matrix[up][i])
                total -= 1
            up += 1
            
            for i in range(up, down+1):
                res.append(matrix[i][right])
                total -= 1
            right -= 1
            
            # there is up += 1 above
            if up <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                    total -= 1
                down -= 1
            
            # there is right -= 1 above
            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                    total -= 1
                left += 1
        
        return res
# @lc code=end

